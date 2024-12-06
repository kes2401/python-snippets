# define function to write to new CSV file including retry attempts in case of error
# 'dataset' variable is assumed to be a Pandas dataframe, and 'output_file_path' a string containing destination path
  
import time

def write_to_csv(dataset, output_file_path, index=False):
    retry_time = 60    # seconds
    max_retries = 3
    retry_attempts = 0
    
    while True:
        try:
            dataset.to_csv(output_file_path, index=index)
            print('Export to CSV file complete.')
            break
        except:
            if retry_attempts >= max_retries:
                print('EXPORT FAILED: Unable to save new CSV file.')
                return
            else:
                time.sleep(retry_time)
                retry_attempts += 1
