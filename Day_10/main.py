import os
import shutil
import csv
import json
from collections import defaultdict
from datetime import datetime

def task1():
    try:
        with open('notes.txt', 'r') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print("File not found")

def task2():
    try:
        with open('poem.txt', 'r') as file:
            line_count = sum(1 for line in file)
        print(f"Total lines: {line_count}")
    except FileNotFoundError:
        print("File not found")

def task3():
    tasks = ["Complete assignment", "Buy groceries", "Call mom", "Exercise", "Read a book"]
    with open('reminder.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def task4():
    new_task = "Water the plants"
    with open('reminder.txt', 'a') as file:
        file.write(new_task + '\n')

def task5():
    filename = 'data.txt'
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            print(file.read())
    else:
        print("File doesn't exist")

def task6():
    try:
        with open('input.txt', 'r') as infile, open('cleaned.txt', 'w') as outfile:
            for line in infile:
                if line.strip():
                    outfile.write(line)
    except FileNotFoundError:
        print("File not found")

def task7():
    try:
        with open('article.txt', 'r') as file:
            content = file.read()
        content = content.replace("Python", "PYTHON")
        with open('article.txt', 'w') as file:
            file.write(content)
    except FileNotFoundError:
        print("File not found")

def task8():
    try:
        with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
            for line in infile:
                outfile.write(line.upper())
    except FileNotFoundError:
        print("File not found")

def task9():
    try:
        with open('students.txt', 'r') as infile, open('report.txt', 'w') as outfile:
            for line in infile:
                name, marks = line.strip().split(',')
                status = "Pass" if int(marks) >= 50 else "Fail"
                outfile.write(f"{name},{marks},{status}\n")
    except FileNotFoundError:
        print("File not found")

def task10():
    try:
        with open('quotes.txt', 'r') as file:
            lines = file.readlines()
        with open('reversed_quotes.txt', 'w') as file:
            file.writelines(reversed(lines))
    except FileNotFoundError:
        print("File not found")

def task11():
    try:
        error_count = 0
        error_lines = []
        with open('server.log', 'r') as file:
            for line in file:
                if "ERROR" in line:
                    error_count += 1
                    error_lines.append(line)
        print(f"Total errors: {error_count}")
        with open('errors_only.log', 'w') as file:
            file.writelines(error_lines)
    except FileNotFoundError:
        print("File not found")

def task12():
    word_count = defaultdict(int)
    try:
        with open('story.txt', 'r') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    word_count[word.lower()] += 1
        with open('frequency.txt', 'w') as file:
            for word, count in sorted(word_count.items()):
                file.write(f"{word}: {count}\n")
    except FileNotFoundError:
        print("File not found")

def task13():
    try:
        with open('sales.csv', 'r') as infile, open('high_sales.csv', 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            header = next(reader)
            writer.writerow(header)
            for row in reader:
                if float(row[1]) > 10000:
                    writer.writerow(row)
    except FileNotFoundError:
        print("File not found")

def task14():
    with open('full_book.txt', 'w') as outfile:
        for chapter in ['chapter1.txt', 'chapter2.txt', 'chapter3.txt']:
            try:
                with open(chapter, 'r') as infile:
                    outfile.write(infile.read())
                outfile.write('\n')
            except FileNotFoundError:
                print(f"{chapter} not found")

def task15():
    folder_path = '.'
    txt_files = [f for f in os.listdir(folder_path) 
                 if os.path.isfile(os.path.join(folder_path, f)) 
                 and f.endswith(('.txt', '.csv'))]
    print("Found files:")
    for file in txt_files:
        print(file)

def task16():
    today = datetime.now().strftime('%Y-%m-%d')
    backup_filename = f"backup/data_backup_{today}.csv"
    try:
        shutil.copy('data.csv', backup_filename)
        print(f"Backup created: {backup_filename}")
    except FileNotFoundError:
        print("File not found")

def task17():
    try:
        with open('raw_text.txt', 'r') as infile:
            lines = infile.readlines()
        with open('formatted_text.txt', 'w') as outfile:
            for line in lines:
                formatted = line.strip().replace('\t', '    ')
                outfile.write(formatted + '\n')
    except FileNotFoundError:
        print("File not found")

def task18():
    with open('chat_log.txt', 'a') as file:
        while True:
            message = input("Enter message (type 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f"[{timestamp}] {message}\n")

def task19():
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            sorted_rows = sorted(reader, key=lambda row: float(row['price']))
        with open('products_sorted.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(sorted_rows)
    except FileNotFoundError:
        print("File not found")

def task20():
    students = []
    try:
        with open('students.txt', 'r') as file:
            for line in file:
                name, age, grade = line.strip().split(',')
                students.append({
                    'name': name,
                    'age': int(age),
                    'grade': grade
                })
        with open('students.json', 'w') as file:
            json.dump(students, file, indent=4)
    except FileNotFoundError:
        print("File not found")

def main():
    print("File Handling Assignment")
    tasks = [task1, task2, task3, task4, task5, task6, task7, task8, task9, task10,
             task11, task12, task13, task14, task15, task16, task17, task18, task19, task20]
    
    while True:
        print("\nEnter task number (1-20) or 0 to exit:")
        try:
            choice = int(input())
            if choice == 0:
                break
            if 1 <= choice <= 20:
                tasks[choice-1]()
            else:
                print("Invalid choice")
        except ValueError:
            print("Please enter a number")

if __name__ == "__main__":
    main()