# Extract_package/src/extract_package/ice_breaking.py

def ice_breaking():
    ascii_1 = '''
 ==++++++*++++++++*#%#==========================
==+++++++++++++++*#%#==========================
+++++++++++++++++*###==========================
+++++++++++====++*###===============-=---=-----
++++++++++======+*######%%%%%##+======---------
+++++++++=======+*#%%%%%%%%%%%%%%#+===---------
++++++++========+#%%%%%#####%%%%%%%#====-------
++++++=+========#%%%%%**++*#####%%%%#+=--------
+++++++========+%%%%#*+++=====+*##%%%%+=-------
*+++++=========*%%%**++++====-==++*%%%%===-----
######*++======%%%*+++++=====-====+*%%%+==-----
%%%%%%#######*#@@#*+++=======--====+#%%+=------
****++*****##%%@#********++=+++++++=+%%+=------
+++++++++++*##*%#*****++++==++**++===#*+=------
+++++++++++***%%*++**#*#++==+**#++===+*====----
++++++++++*+++*#*+++++++*+==+=++=====+=-==-----
++++++++++++++#+*++====+*+=====================
++++++++++++++***++====**+===++=====+==========
*+++++++++++++++*+++===+***+========#+=========
*****++++++++++**+++++*+++===+++===*%+=========
*******+++++++++*#*++**#**+++***+=***==========
*********+++++++*#%**+++***+==+++*%+===========
**********+++++*%%%##**++++==+++=*#*-==========
******+++===+==%%%%##*******++==+###--=--======
***+===========%%%%%#*****++===*####--==-=---==
*========-====+%%%%%#*+++++===+#####--====--===
========--=-=-*#%#%%#+========#####%--==-=---==
=======---=--=########=======*##%###--+===--===
=====-=---=--=########+=====+###%##%--+===--===
======---=---+########*=====####%###==+====-==-
==========-==##########+===*####%##%==+==+=====
==========-=###########%==*#####%##%*=+==++====
========+==*####%##%###%**######%##%#=+==++====
========+==###########%%#####%##%##%#**+-++====
''' 

    ascii_2 = '''
.............................................................
.............................................................
.............................................................
.............................................................
........................:=*#*+######+:.......................
......................-#%%###%#%#######=.....................
.....................*%%%%%##%*%%%%%%%%%%-...................
...................:%%@@@%%#%%*#%%%%@@@%%%=..................
..................:*%%%%%%#*+=--==+*%%@@%%%+.................
..................=%%%%%%+=::::..:::-+%@@%@%-................
.................:%%%%%%=-::.......:::-#@@@@#................
.................#@%%%%=---:::..::::----%@@@@=...............
................:%@%%#=:::::--:::--:::::=@@@@%:..............
................=%%+%+:-+=#+=-:.:-=#*+=::#%#@%+..............
................+%%*#+:::::::::.:::::::::*#%@%*..............
................+%%%+=:::::::::.:::::::::#%@@@#:.............
...............-*%%%@*-:::::::::-:::::::-@@@@%*..............
...............-#%%%@%=::::::----:::::--*@@%@%*..............
...............-#%%%@@#-:::--=====--:--=@@@%%#-..............
...............-#%#%%%@#-----====-----=@@@@%%#=..............
...............:*#%%%@@@%=-::::::::-=*@@@@@@%#*:.............
................+###%%@@%+++------=+=*@@@%%@%%##:............
................-*##%%@@%+===========*@@@%%%%####+...........
................+*##%%@@%+=-=-----===*@@@@%%%%%%%%+..........
..............-####%%%%%%*=-------==+%@@%@%%%%%%%%#:.........
.............=**#*#%%%%%##+=------+*%%%%%%%%%@%%%%+-.........
............**#**#%%%%%%%*+=-----=#%%%##%%##%%####=..........
...........=######%%%%%%%#*=-----=#%%%%%%##%%%%%#+...........
...........-####*#%%%%%%%##+-:::-=#%%%%%##%%%%%%#+-..........
...........:=##*+#########*+-::::-+*%%%###%%#*++--:..........
.............:=****##%####+=-:::::--=*%%###*++=-::...........
................-*%%%%%%###-:......-:-*####%#*=::............
.................-*#%@%#*++*:.......::-+##%%#-::::...........
..................-*##***+++-.........:=*#%%*:..::...........
............:......:=*##*+=-:.........=*###*::..:............
............:........:-=++=-:.......:-++++-:...::..::........
............:..................................::.........::.
...............................................::........:::.
............:..................................:::......::...
............::.................................::::.....::.:.
.............:..............................:..:::.....::::::
'''

    ascii_3 = '''
⡣⡃⡣⡃⡃⡣⡃⡣⡑⡑⢕⢑⢕⢑⢕⢑⢑⢑⢑⢑⢑⢑⢑⢑⠅⠕⠅⢕⢑⠅⠕⠅⠕⠅
⡪⡨⡨⡨⡨⡨⡨⡨⠨⠪⡢⡡⣑⡥⣕⣵⣧⡷⣵⢵⣥⡡⡑⡐⠅⠕⠅⢕⢐⠅⠅⠕⠅⠅
⡢⡂⡂⡂⡂⡂⡂⡊⡪⡨⣪⡾⣯⢿⡽⣷⣻⣟⣿⢯⣷⣻⣳⣕⢕⠅⠅⢕⢐⠅⠅⠅⠅⠅
⡂⡂⡂⡂⡂⡂⡂⡂⣢⣯⢯⡿⣽⣻⣯⣿⣽⣯⡿⣯⢿⣳⣿⣺⡷⡅⢅⠑⠄⠅⠅⠅⠅⠅
⡂⡂⡂⡂⡂⡂⠢⠨⣾⡽⣯⣟⡷⣟⣷⢿⡾⣷⣟⣿⣻⢯⡷⣿⢽⣟⠄⠅⠅⠅⠅⠅⠅⠅
⡐⡐⡐⡐⡐⠌⠌⢬⣷⡿⣿⢽⣯⣻⣝⡯⣟⣗⣟⣮⢯⣯⡯⣟⣯⡿⡎⠌⠌⠌⠌⠌⠌⠌
⡂⡂⡂⠢⠨⠨⠨⢸⡷⣿⣟⣿⣳⡷⡗⣟⣷⠵⣗⢿⢽⣽⢿⡽⣷⣟⠇⠅⠅⠅⠅⠅⠅⠅
⡂⠢⠨⠨⠨⠨⢈⢂⢿⣻⢼⡼⣔⢅⣕⢕⣕⣍⢎⢎⡅⡕⣭⣝⡿⡞⠅⠅⠅⠅⠅⠅⠅⠅
⠠⠡⠡⠡⠡⢁⢂⠘⡆⡽⡌⡇⡣⡣⡣⡱⡢⡚⡔⡱⡑⠕⡜⢔⡏⡪⠨⠨⠨⠨⠨⠨⠨⠨
⠨⠨⠨⠨⠨⢐⢐⢐⢸⢸⢸⢸⠨⠨⠨⡸⡐⡐⠄⠅⢅⠑⢌⢆⠕⠌⠌⠌⠌⠌⠌⠌⠌⠌
⠅⠅⠅⠅⡁⢂⠂⡂⢂⢑⢱⢱⢑⠅⠕⢕⢇⢚⢘⢌⠢⠡⠡⡣⠡⠡⠡⠡⠡⠡⠡⠡⠡⢁
⠠⠁⠌⡀⢂⠐⡀⠂⡐⢀⠂⢇⢇⢇⢧⢣⠦⡱⢔⢔⠅⢕⠕⠄⠡⠁⠅⠡⠁⠅⠅⠅⠅⡂
⠨⢀⠡⠐⠠⠐⢀⠁⠄⢐⢐⢸⢸⢸⢸⢸⠸⡘⢔⢕⢕⢕⢅⠡⠈⠄⠡⠈⠄⠡⠁⠅⡁⡂
⠐⢀⠐⢈⠠⠈⡀⠄⠂⡐⡀⡇⡇⡇⡇⡇⡇⡎⡆⡕⢕⢕⢱⠡⠁⠌⠐⡈⠠⠁⠌⡀⢂⠐
⢈⠀⡐⢀⠐⠠⢐⠨⢐⢐⠠⢱⠱⡨⠪⠪⠪⡊⡪⡈⡂⡂⡪⠨⠨⠠⠡⢐⢀⠡⠐⢀⠂⡈
⠀⠄⢂⠐⠨⠐⡐⠨⠐⡐⠨⠀⠣⡪⠨⡈⡂⡂⡂⡂⡂⡢⠃⠨⠨⢈⠨⠐⡐⡈⠌⡀⢂⠐
⠁⠅⢐⠈⠌⠄⢂⠨⠀⡂⠅⢌⠢⡑⡑⡐⡐⡐⡐⡐⡰⡈⢄⠅⠅⡂⠄⠅⡐⢐⠐⡐⢐⠐
⠅⠨⠀⡂⠡⠈⠄⢂⠡⠀⠅⢂⢑⠐⠄⡂⢂⢂⠂⡂⢂⠨⠀⡈⠄⠐⡀⠡⠠⠐⡀⢂⠐⡀
⠨⢀⠡⠐⡈⠄⠡⠐⡀⠅⡈⠄⠐⡀⠡⢐⠀⠂⠂⠠⠀⡐⠀⠄⢂⠡⠐⢀⠁⡂⠄⠂⢐⠠
⠐⡀⢐⠠⠐⠐⡈⠄⠐⡀⢐⠈⠠⠐⠀⡂⠀⠂⢁⠈⠄⠐⢈⠀⢂⠐⢈⠠⠠⠀⠂⡁⠄⠂
⡁⠄⠄⠂⡈⠄⠐⡈⠠⠐⡀⠌⠐⡈⠠⠐⠀⢁⠠⠐⢀⠁⠄⢈⠠⠐⢀⠐⠐⢈⠠⠀⢂⠁
⠀⠂⠂⡁⠄⠨⠠⠐⢀⠡⠀⠂⡁⠄⠂⠡⠈⢀⠐⢈⠠⠐⢈⠠⠐⢈⠠⢀⠁⠄⠐⢈⠠⠐   
'''   
