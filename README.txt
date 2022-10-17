[How to run this search engine] (Local GUI)
1. Make sure you have downloaded the “DEV” folder and make a directory called “cache” to store all partial files and indexing data pickle files
2. Run “InvertedIndex.py”
3. The file named “inverted_index.txt” will be generated after full execution of the program. (this will probably take 15~30 minute depending on your system *this is based on our team members environment)
4. Run “search_gui.py”
5. Tkinter window will pop up and type the desired query in the entry box.
6. Click the ‘show the result’ to see the result of your query.
7. Exit by pressing the ‘esc’ button or close the window by mouse click.

*If you want to run the program on the console, follow the instructions up to 3, and run “search.py” instead of following the rest of the instruction lines. You can now follow the instructions printed out in the console window.

[How we created our inverted index]
First of all, for in-memory efficiency,  we set our counterLimit to 10000. This counter limit makes our program stop and store the inverted index information  for every 10000 json files into a txt file. As we tested many different limits with the fact that a single json file usually takes 0.01 to 0.05 MB during the construction of the inverted index, we ended up setting our json counter to 10000, and it gave a reasonable efficiency that the memory usage is evenly distributed with the memory usage of 200MB~350MB for creating the whole inverted index. 
As we run "InvertedIndex.py,” we obtained 6 partial text files, and they effectively store all information about the whole inverted index. Then, we sorted the partial files separately for memory efficiency and then merged them as 'inverted_index.txt.’ Besides the partial files, we managed the other indexing data by storing three pickle files as “indexGuide.pkl”, urlMap.pkl” and “totalNumDocs.pkl” in the “./cache” directory. You would see 'inverted_index.txt' be generated in the directory that "InvertedIndex.py" is placed in. 
