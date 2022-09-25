I've used the fixer.io API to calculate the currency conversion. It requires
registration to receive a personal secret key.

Once you've registered, run pip install python-dotenv

Dotenv allows us to keep environment variables in their own file and prevents
them from being shared with others

Once installed, create a .env file, and include the text KEY="YOUR_KEY"

This will allow the converter to pull in your personal key

All supported symbols are included in symbols.json