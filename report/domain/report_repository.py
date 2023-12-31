from django.shortcuts import get_list_or_404
from report.domain import Report

class ReportRepository:
    def find_pending_reports_with_comment(self):
        return get_list_or_404(Report.objects.select_related('comment').order_by('-reported_at'), state='PENDING')