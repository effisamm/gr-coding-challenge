import csv
from datetime import datetime
import ijson
import os


class ReportSummary:
    def __init__(self, session_id, start_time, end_time, duration, returned_late, damaged_on_return):
        self.session_id = session_id
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.returned_late = returned_late
        self.damaged_on_return = damaged_on_return


def extract_transform_json_file(file_path):
    report_summary = []
    rental_data = {}
    session_id = None

    with open(file_path, "r") as json_file:
        parser = ijson.items(json_file, "item")
        for rental_data in parser:
            if "type" in rental_data and rental_data["type"] == "START":
                start_time = datetime.utcfromtimestamp(int(rental_data["timestamp"]))
                session_id = rental_data["id"]

            elif "type" in rental_data and rental_data["type"] == "END":
                rental_data["type"] = "END"
                rental_data["id"] = session_id
                comments = rental_data.get("comments", "")
                end_time = datetime.utcfromtimestamp(int(rental_data["timestamp"]))
                try:
                    if end_time > start_time:
                        duration = (end_time - start_time).total_seconds() / 3600
                        returned_late = duration > 24
                        damaged_on_return = (comments.strip() != "")
                        car_report_summary = ReportSummary(session_id, start_time, end_time, duration, returned_late,
                                                   damaged_on_return)
                        report_summary.append(car_report_summary)
                    else:
                        print("Error in timestamp at point of return for {}". format(session_id))
                except Exception as e:
                    print("Error processing session {}: {}".format(session_id, e))

    return report_summary


def load_summaries_to_csv(output_file_path, report_summary):
    with open(output_file_path, "wb") as output_file:
        save_summaries = csv.writer(output_file)
        save_summaries.writerow(["Session ID", "Start Time", "End Time",
                                 "Duration", "Returned Late", "Damaged On Return"])
        for i in report_summary:
            save_summaries.writerow([i.session_id, i.start_time, i.end_time, i.duration,
                                     i.returned_late, i.damaged_on_return])


if __name__ == "__main__":
    # Move 2 directories up to get analyze_car_rentals absolute path
    current_dir = os.getcwd()
    child_current_dir = os.path.dirname(os.path.abspath(os.path.join(current_dir, os.pardir)))
    parent_current_dir = os.path.dirname(os.path.abspath(os.path.join(child_current_dir, os.pardir)))

    file_path = os.path.join(parent_current_dir, "car_rentals_etl_job\\data\\rental_reports.json")
    output_file_path = os.path.join(parent_current_dir, "car_rentals_etl_job\\data\\rental_reports.txt")
    summaries = extract_transform_json_file(file_path)
    load_summaries_to_csv(output_file_path,summaries)