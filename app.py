from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('cases.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    case_details = None
    not_found = False
    
    if request.method == 'POST':
        fir_number = request.form['fir_number']
        # Ensure the FIR number is an integer
        try:
            fir_number = int(fir_number)
            # Search for the FIR number in the DataFrame
            case = df[df['FIR_Number'] == fir_number]
            
            if not case.empty:
                case_details = case.iloc[0].to_dict()
            else:
                not_found = True
        except ValueError:
            not_found = True
    
    return render_template('index.html', case_details=case_details, not_found=not_found)

if __name__ == '__main__':
    app.run(debug=True)
