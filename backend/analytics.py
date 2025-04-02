class JobAnalytics:
    def get_report(self):
        total_jobs = jobs_collection.count_documents({})
        total_applied = applications_collection.count_documents({"status": "applied"})
        success_rate = applications_collection.count_documents({"status": "interview"}) / total_applied * 100

        return {
            "total_jobs_found": total_jobs,
            "total_jobs_applied": total_applied,
            "success_rate": f"{success_rate:.2f}%"
        }

