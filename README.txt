HOW TO RUN:
To run the entire assignment open the current directory in terminal and type ./assign2. If the terminal says permission denied type chmod +x assign2 and enter , after which the command ./assign2 should run. This command will run each problems shell file and their corresponding ouputs will be saved in the current directory.

Dependencies:
In this assignment numpy, pandas, scipy and xlrd are used. All the necessary files required to run the assignment is included.

Content:
In this assignment there are 9 problems to be solved. For every problem i've included their shell script as instructed so for running a specific problem , cd into the current directory and type ./question name , for example -  ./gender-india.

1. First problem is percent-india where we have to find the percentage of people speaking three and exactly two and exactly one language. The scripts name is percent-india.sh which after being run will produce the output file percent-india.csv. For people speaking exactly one language is calculated by subtracting the people speaking atleast two languages from the total population and for exactly two language , it will be atleast two substracted from atleast three.

2. Second problem is of the same nature as above question, but we have to find the p-value for stating if there is any statistic difference between the male and female ratio. i have used the ttest from scipy using the total male by total female as the popmean. The file's name is 
gender-india.sh and after running it will produce three ouput files named gender-india - {part}.csv where part refers to the monolingual or bilingual or trilingual.

3. Third problem is same as both the first and second problem where we have to find the statistic difference between the urban and rural ratio. files name is geography-india.sh and it will produce three files geography-india-{part}.csv , where part refers to the monolingual or bilingual or trilingual.

4. Fourth question is about finding three best and three worst states in terms of ratio of people speaking three langauge by people speaking two languages. i used the same way in first question to find number of people speaking two languages, files name is 3-to-2-ratio.sh and it will produce 3-to-2-ratio.csv . Another part of this problem is to find the same three worst and best states according to the  number of people speaking exactly two languages by people speaking exactly one language. The files name is 2-to-1-ratio.sh and will produce 2-to-1-ratio.csv.

5. Fifth question is about finding the age groups having the highest percentage of people speaking three or more language i solved this question by first finding the percentage of people speaking three or more languages in every group in every state or union territory or india then i i found the maximum value of percentage in every group(state or union territory or india) , files name is age-india.sh and it will produce age-india-csv.


6. sixth question is of the same nature as fifth question, in this question we have to find the literacy group having the highest percentage of people speaking three or more language .  I solved this question by first finding the percentage of people speaking three or more languages in every literacy group for every state or union territory or india then found the maximum value of percentage in every group(state or union territory or india) . Files name is literacy-india.sh and it will produce literacy-india-csv.

7. Seventh question is about finding the topmost three spoken language in each region and has two parts first one is using the mother tongue and second one uses all three languages. I solved the first part by finding the most spoken language in the region and when ever top three had same languages i added them. The second part is solved similary by adding the same language speakers and then finding the top three. Files name is  region-india.sh and it will produce two csv files named region-india-{part}.csv where part refers to the division of the problem to mother tongue only and all three languages.

8. This question is about finding the age group having the highest ratio of population speaking three languages and we have to repeat it for exactly two and one languages. This question is the extension of the fifth question with the diference of males and females but not for the whole population. Files name  is age-gender.sh. and it will produce three csv files names age-gender-a.csv and age-gender-b.csv  and age-gender-c.csv 

9 . This question is about finding the literacy group having the highest ratio of population speaking three languages and we have to repeat it for exactly two and one languages. This question is the extension of the sixth question with the difference of males and females but not for the whole population. Files name  is literacy-gender.sh and it will produce three csv files names literacy-gender-a.csv and literacy-gender-b.csv and literacy-gender-c.csv 















































