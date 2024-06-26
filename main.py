import time
import concurrent.futures
from selenium.common.exceptions import WebDriverException
from input_data import destinations, check_in_date, check_out_date
from handle_form import search_hotels
from save_to_csv import save_to_csv
from extract_hotel_data import extract_hotel_data
from load_driver import load_driver
from logger import set_log

# Initialize the custom logger
logger = set_log()

def process_destination(destination, check_in_date, check_out_date, max_retries=3):
    """
    Process each destination to search hotels, extract data, and save to CSV.
    
    Args:
    - destination: Destination name.
    - check_in_date: Check-in date.
    - check_out_date: Check-out date.
    - max_retries: Maximum number of retries for network-related issues.
    """
    retries = 0

    while retries < max_retries:
        try:
            driver = load_driver()  # Load driver here to ensure a fresh instance per task

            # Search Hotels
            search_hotels(driver, destination, check_in_date, check_out_date)

            # Get Hotel Data
            hotel_data = extract_hotel_data(driver, destination, check_in_date, check_out_date)

            # File Name
            file_name = generate_file_name(destination, check_in_date, check_out_date)

            # Save Hotel Data
            save_to_csv(destination, hotel_data, filename=file_name)

            break  # If successful, break out of the retry loop

        except IndexError as ie:
            error_msg = f"IndexError for {destination}: {str(ie)} - Passing."
            logger.error(error_msg)  # Log the error
            pass  # Just pass on IndexError

        except (WebDriverException, Exception) as e:
            error_msg = f"Exception occurred for {destination} (attempt {retries + 1}): {str(e)}"
            logger.error(error_msg)  # Use the custom logger
            retries += 1
            time.sleep(10 + retries * 5)  # Exponential backoff

        finally:
            driver.quit()  # Quit the driver after processing each destination
            logger.info("Quit WebDriver")

            # time.sleep(30)  # Wait before the next task

def generate_file_name(destination, check_in_date, check_out_date):
    """
    Generate a CSV file name based on destination and dates.
    
    Args:
    - destination: Destination name.
    - check_in_date: Check-in date.
    - check_out_date: Check-out date.
    
    Returns:
    - str: Generated file name.
    """
    formatted_destination = destination.replace(", ", "_").replace(" ", "_")
    formatted_check_in = check_in_date.replace("/", "_")
    formatted_check_out = check_out_date.replace("/", "_")
    return f'{formatted_destination}_{formatted_check_in}_To_{formatted_check_out}.csv'

def main():
    """
    Main function to iterate over destinations and process each one in parallel.
    """
    start_time = time.time()  # Start the timer

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        futures = [
            executor.submit(process_destination, destination, check_in_date, check_out_date)
            for destination in destinations
        ]
        
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                logger.error(f"Exception occurred during parallel processing: {str(e)}")

    end_time = time.time()  # End the timer
    execution_time = end_time - start_time
    logger.info(f"Execution time: {execution_time} seconds")  # Log execution time

if __name__ == '__main__':
    main()
