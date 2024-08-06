from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        # Add a header to the PDF
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "CS50 Shirtificate", 0, 1, "C")

    def create_shirtificate(self, name):
        # Set up the PDF
        self.add_page("P", (210, 297))  # A4 size in mm (portrait orientation)
        self.set_auto_page_break(auto=True, margin=15)

        # Add the CS50 shirt image
        self.image("shirtificate.png", x=40, y=80, w=130)

        # Add the user's name on top of the shirt in white text
        self.set_text_color(255, 255, 255)  # White color
        self.set_font("Arial", "", 24)
        self.cell(0, 50, name, 0, 1, "C")

if __name__ == "__main__":
    name = input("Enter your name: ")

    # Create the shirtificate PDF
    shirtificate = Shirtificate()
    shirtificate.create_shirtificate(name)

    # Output the PDF to a file
    shirtificate.output("shirtificate.pdf")
