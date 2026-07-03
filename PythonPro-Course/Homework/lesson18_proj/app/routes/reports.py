from flask import Blueprint, request, send_file
from .utils import http_err
from ..services.report_service import generate_monthly_report_pdf
reports_bp = Blueprint("reports", __name__, url_prefix="/api/reports")
@reports_bp.route("/monthly", methods=["GET"])
def monthly_report():
    month = request.args.get("month")
    if not month:
        return http_err("Brakuje parametru month", 400)
    try:
        pdf_buffer = generate_monthly_report_pdf(month)
        return send_file(
            pdf_buffer,
            as_attachment=True,
            download_name=f"monthly_report_{month}.pdf",
            mimetype="application/pdf",
        )
    except ValueError as e:
        return http_err(str(e), 400)