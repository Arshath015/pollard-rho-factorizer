import requests

def main():
    n = 8051
    response = requests.post('http://localhost:8000/factor', json={'n': n})
    factors = response.json()['factors']
    print(f'The factors of {n} are {factors}')
if __name__ == '__main__':
    main()