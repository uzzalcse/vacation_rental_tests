import pandas as pd
import os
import time
from openpyxl import load_workbook
from openpyxl.utils.exceptions import InvalidFileException

def save_results_to_excel(results, file_name="reports/test_results.xlsx", sheet_name="url status test", max_retries=3):

    # Ensure the 'reports' directory exists
    os.makedirs(os.path.dirname(file_name), exist_ok=True)

    # Convert results to a DataFrame
    df = pd.DataFrame(results)
    
    for attempt in range(max_retries):
        try:
            # If file exists and is not empty
            if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
                try:
                    # Try to read existing file
                    existing_df = pd.read_excel(file_name, sheet_name=None)
                    
                    # Create a new Excel file while preserving other sheets
                    with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
                        # Write all existing sheets except the current one
                        for existing_sheet in existing_df.keys():
                            if existing_sheet != sheet_name:
                                existing_df[existing_sheet].to_excel(writer, sheet_name=existing_sheet, index=False)
                        # Write the new sheet
                        df.to_excel(writer, sheet_name=sheet_name, index=False)
                    return  # Success, exit function
                except Exception as e:
                    print(f"Error reading existing file: {str(e)}")
                    # If error occurs, create new file with just this sheet
                    df.to_excel(file_name, sheet_name=sheet_name, index=False)
                    return
            else:
                # If file doesn't exist or is empty, create new
                df.to_excel(file_name, sheet_name=sheet_name, index=False)
                return  # Success, exit function
                
        except Exception as e:
            if attempt < max_retries - 1:  # if not the last attempt
                print(f"Attempt {attempt + 1} failed: {str(e)}")
                time.sleep(1)  # Wait before retrying
                # If file is corrupted, remove it and try again
                if os.path.exists(file_name):
                    try:
                        os.remove(file_name)
                    except Exception:
                        pass
            else:
                print(f"Final attempt failed: {str(e)}")
                # On final attempt, try to create new file with just this sheet
                try:
                    df.to_excel(file_name, sheet_name=sheet_name, index=False)
                except Exception as final_e:
                    print(f"Could not create new file: {str(final_e)}")
                    raise