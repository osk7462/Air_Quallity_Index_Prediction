from bs4 import BeautifulSoup


def extract(file_name):
    data = ""
    with open(file_name) as file:
        soup = BeautifulSoup(file, "html.parser")
        rows = soup.find_all('tr')
        k = 0
        for row in rows:
            if k != 0:
                data += '\n'
            k += 1
            for i in row:
                try:
                    data += i.text + " "
                except AttributeError:
                    pass

    with open("text.txt", "w") as text:
        text.write(data)
    data = []
    with open("text.txt", "r") as myfile:
        for line in myfile:
            ok = line.split(" ")
            data.append(ok)
    return data

