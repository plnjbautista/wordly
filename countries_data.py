# countries_data.py
"""
 class CountriesDataManager is a class to manage a dataset of countries and provide efficient methods for querying and organizing the data.
    
    This class performs the following functions:
    1. Loads a predefined list of country names and stores them in a lowercase format.
    2. Indexes the countries by their starting letter for quick lookups.
    3. Provides methods to:
       - Retrieve all countries.
       - Get countries starting with a specific letter.
       - Check if a country exists in the dataset.
       - List all available starting letters for countries.
    
    The dataset of countries is loaded from a hardcoded list in the _load_countries_data() method.
    The indexing of countries by their starting letter is done to facilitate faster lookups when searching for countries that begin with a specific letter.
    
    Methods:
    - get_all_countries(): Returns a list of all countries.
    - get_countries_by_letter(letter): Returns countries that start with a specific letter.
    - is_valid_country(country_name): Checks if a country name exists in the dataset.
    - get_available_starting_letters(): Returns a list of letters that have at least one country associated with them.
    """
class CountriesDataManager:
    
    def __init__(self):
        """Initialize the countries data manager"""
        self.countries_data = self._load_countries_data()
        self.countries_by_letter = self._index_countries_by_letter()
    
    def _load_countries_data(self):
        """Load the countries dataset"""
        # Real-world implementation would load from a CSV or API
        # For simplicity, using a predefined list here
        countries = [
            "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", 
            "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", 
            "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", 
            "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", 
            "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", 
            "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", 
            "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", 
            "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica", 
            "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", 
            "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", 
            "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", 
            "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", 
            "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", 
            "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", 
            "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", 
            "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", 
            "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", 
            "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", 
            "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", 
            "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", 
            "Nigeria", "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", 
            "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", 
            "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", 
            "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", 
            "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", 
            "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", 
            "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", 
            "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", 
            "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", 
            "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", 
            "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", 
            "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", 
            "Yemen", "Zambia", "Zimbabwe"
        ]
        return [country.lower() for country in countries]
    
    def _index_countries_by_letter(self):
        """Index countries by their starting letter for quicker lookups"""
        letter_index = {}
        for country in self.countries_data:
            first_letter = country[0].lower()
            if first_letter not in letter_index:
                letter_index[first_letter] = []
            letter_index[first_letter].append(country)
        return letter_index
    
    def get_all_countries(self):
        """Return all countries"""
        return self.countries_data
    
    def get_countries_by_letter(self, letter):
        """Return countries starting with the given letter"""
        return self.countries_by_letter.get(letter.lower(), [])
    
    def is_valid_country(self, country_name):
        """Check if a country name exists in the database"""
        return country_name.lower() in self.countries_data
    
    def get_available_starting_letters(self):
        """Get all letters that have at least one country"""
        return list(self.countries_by_letter.keys())