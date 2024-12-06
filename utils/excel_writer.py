import pandas as pd

def write_to_excel(filename, results_by_url):
    with pd.ExcelWriter(filename, engine="xlsxwriter") as writer:
        for url, results in results_by_url.items():
            # Prepare the data for each URL in a dataframe
            data = []
            for result in results:
                data.append({
                    "Page URL": url,
                    "Test Case": result["test_case"],
                    "Status": result["status"],
                    "Comments": result["comments"]
                })
            
            # Extract a meaningful sheet name from the URL
            # Ensure the URL has enough segments
            url_parts = url.split("/")
            if len(url_parts) > 4:
                sheet_name = url_parts[4]  # Use the 5th part of the URL as the sheet name
            else:
                sheet_name = "Other"  # Default sheet name if not enough segments
            
            # Create a DataFrame and write it to a separate sheet
            df = pd.DataFrame(data)
            df.to_excel(writer, sheet_name=sheet_name, index=False)
