#!/usr/bin/env python3
import ipdb
import sys
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from lib.Author import Author
from lib.Magazine import Magazine


if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###
    
    author1 = Author("Author 1")
    author2 = Author("Author 2")

    
    magazine1 = Magazine("Magazine 1", "Category 1")
    magazine2 = Magazine("Magazine 2", "Category 2")

    
    article1 = author1.add_article(magazine1, "Article 1")
    article2 = author2.add_article(magazine2, "Article 2")
    article3 = author1.add_article(magazine1, "Article 3")

   
    print(author1.name())  
    print(author1.articles())  
    print(author1.magazines())  
    print(author1.topic_areas())  

    print(magazine1.name())  
    print(magazine1.category())  
    print(Magazine.all())  
    print(Magazine.find_by_name("Magazine 1")) 
    print(Magazine.article_titles())  
    print(magazine1.contributors())  

# DO NOT REMOVE THIS
    ipdb.set_trace()
