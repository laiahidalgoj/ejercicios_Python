import sqlite3

def main():
    #create_pupil(8, 'rosa', 'camacho')

    print(find(id=1, name='laia', surname='hidalgo'))

    conn = sqlite3.connect('pupils.db')
    cursor = conn.cursor()

    cursor.close()
    conn.close()


def create_pupil(id, name, surname):
    conn = sqlite3.connect('pupils.db')
    cursor = conn.cursor()

    query = '''INSERT INTO pupils(id, name, surname) VALUES(?, ?, ?)'''

    rows = cursor.execute(query, (id, name, surname))

    conn.commit()
    cursor.close()
    conn.close()

def find(id, name, surname):
    conn = sqlite3.connect('pupils.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM pupils WHERE id='{id}' AND name='{name}' AND surname='{surname}'"
    cursor.execute(query)

    result = cursor.fetchone()
    return result

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()