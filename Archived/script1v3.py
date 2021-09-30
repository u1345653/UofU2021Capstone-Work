### NAME: RICKY SNYDER
# TITLE: BUILDING FIRST WEBSITE WITH FLASK WEBSITE FRAMEWORK
# PURPOSE: BUILD UPON INTRODUCTION TO WEB PAGE DEVELOPMENT, BY INCORPORATING HTML FILES & CODE RATHER THAN TRANSPOSING TEXT OBJECTS FROM PYTHON ONTO WEBPAGE!
# VERSION: 3.0
# DEPENDENCIES: 'PIP INSTALL FLASK' IN CMD TO INSTALL NECESSARY FLASK LIBRARY

# STEP 1 - IMPORT INSTALLED CLASSES NEEDED FROM FLASK LIBRARY
from flask import Flask, render_template      # IMPORTING THE FLASK CLASS TO IMPORT OUR FLASK OBJECT
                                              # & IMPORTING RENDER_TEMPLATE CLASS ENABLING OUR HTML CAPABILITIES

# STEP 2 - CREATE A VARIABLE CONTAINING OUR FLASK OBJECT, WHICH PASSES THE 'NAME' PARAMETER
app = Flask(__name__)                  # VARIABLE NAME 'NAME' INSTANTIATES OUR APP FLASK OBJECT

########################################################################################################################
########                             BUILDING OUT OUR MULTIPLE WEBPAGES!                                        ########
########################################################################################################################

# STEP 3 - DEFINE THE APP.ROUTE() METHOD - WHICH ALLOWS US TO IDENTIFY THE URL STRING WE WANT REPRESENTING A WEBPAGE
@app.route('/')                             # EXAMPLE URL STRING FOR A HOME PAGE; JUST PASSING '/' AS PARAMETER

# STEP 4 - CALLING FUNCTION THAT REFERS TO .HTML DOCUMENT, RATHER THAN JUST PRINTING THE TEXT IN THE 'RETURN' STATEMENT
def home():
    return render_template('home.html')            # FILE PATH OF DESIRED .HTML FILE (WHICH WE'LL BUILD OUT IN HTML)

# STEP 5 - DEFINING APP.ROUTE (WEBPAGE) #2 - OUR ABOUT PAGE!
@app.route('/about/')         # DEFINING OUR ABOUT URL PAGE!

# STEP 6 -  CALLING FUNCTION THAT REFERS TO OUR ABOUT.HTML PAGE
def about():
    return render_template('about.html')           # FILE NAME OF DESIRED ABOUT HTML WEBPAGE TO BE TRANSPOSED TO WEBSITE!

# STEP 6 - DEFINING CONDITIONAL THAT TRIGGERS OUR WEB APP TO RUN WHEN TRUE
if __name__ == "__main__":              # WE WANT OUR WEB APP TO RUN, IF THE __NAME__ VARIABLE CONTAINS THE __MAIN__ ARGUMENT (FOR NOW)
    app.run(debug=True)                 # CALLING THE .RUN() METHOD ON OUR FLASK OBJECT, WHICH ALLOWS US TO OPEN THE WEBPAGE FROM PORT 5000