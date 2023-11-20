# WebScraper in python
This is a simple webscraper I made in python, for fun.
This webscraper, scraps DMR's webpage for vehicle information.

## How to
First you need to install:

```
pip install requests beautifulsoup4
```
```
pip install selenium
```

And then to need to enter a registraion number at:

```
def main():
    registration_number = "xx12345"
    data = fetch_vehicle_data(registration_number)

```
Keep in mine it only works on Danish registration numbers

## Additional information
Right now it only find the baisc infomation about the vehicle. You could always expand it further.
