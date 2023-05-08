import subprocess
import os
import time



def get_page():
    if check_file_modified('dram.txt'):
        # Run the curl command to fetch the HTML page and pipe it to xmllint
        curl_command = ['curl', '-s', 'https://mironline.ru/support/list/kursy_mir/']
        xmllint_command = ['xmllint', '--html', '--xpath', '/html/body/div[3]/div[2]/div[1]/div/div/div/div/div[2]/table/tbody/tr[2]/td[2]/span/p/text()', '-']
        p1 = subprocess.Popen(curl_command, stdout=subprocess.PIPE)
        p2 = subprocess.Popen(xmllint_command, stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

        # Get the result as a string
        result = p2.communicate()[0].decode().strip()
        dram = result.split('\n')[1].strip().replace(',', '.')
        with open('dram.txt', 'w') as f:
            f.write(dram)
        return dram
    return read_file()



# Check if the file was modified more than 12 hours ago
def check_file_modified(file):
    mod_time = os.path.getmtime(file)
    current_time = time.time()
    if (current_time - mod_time) > 4*3600: # 12 hours in seconds
        return True
    else:
        return False
def read_file():
    with open('dram.txt', 'r') as f:
        return f.read()


# print(check_file_modified('dram.txt'))
# print(get_page())