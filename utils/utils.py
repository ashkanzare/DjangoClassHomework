import threading
from pathlib import Path
from pdfkit import from_string


class MakePDF(threading.Thread):
    def __init__(self, html, student):
        self.html = html
        self.student_id = student.id
        threading.Thread.__init__(self)

    def run(self):
        print(self.html, '\n++++++++++++++++++++++++++++', self.student_id)
        """Generate a PDF file from a string of HTML."""
        path = f'media/std_results/std_{self.student_id}.pdf'
        from_string(self.html, f'../media/std_results/std_{self.student_id}.pdf')


def create_pdf(html, student):
    MakePDF(html, student).start()

