# COS226HashTableHW

Jennifer Morin                                                     README Reflection
11/25/2025                                                                    COS226

Method 1 - The first method I tried was to have my hash function take the name or quote
    from the movie and convert all characters into their ascii codes. Then when adding
    the data item into the table I would add it into the list using the predetermined
    key as the index. When collisions happened, as two data items came out as the same
    after the hash function I handled the issue using the linear probing technique. 
    There were many issues that became apparent in the results, primarily the amount 
    of time that was required and the huge amount of memory needed to instantiate the
    table. Overall this method would not be ideal for most scenarios other than 
    simplicity of coding because as the amount of data went up the collisions would
    happen more often and more spaces would fill just prolonging the time required.
    There is also an issue that would be found as you tried to search in the function
    because due to the linear probing technique combined with the amount of collisions
    there would be a huge amount of data not present in or next the key it is supposed
    to have the index of.

    The results using the movie titles were:
    Collisions: 13328
    Empty Spots: 44494
    Time used: 6.39 Seconds
    The results using the movie quotes were:
    Collisions: 13769
    Empty Spots: 4332430
    Time used: 6.69 Seconds

Method 2 - Similarly to my first method my second attempt at optimizing the hash table
    utilized a linked list approach. The hash function remained the same between 
    method 1 and 2 but when collisions happened the code would first identify whether 
    or not a list is present in the index given by the key. If the index was already a
    list then the data item would just be appended to the end of it and if it was an 
    item present then a list would be created using the original data item and the 
    item being added in. There was definitely improvement in both the amount or time
    required to create the hash table and in the number of collisions that the hash
    table had to fix. One area that continued to present itself as a problem though
    was the amount of memory required of the functions and therefore the amount of
    empty memory that does not have any use. Compared to the basic linear probing 
    method there is definitely some improvements but because of the issues still with
    space the basic linked list approach would only be useful where time is the only 
    important factor or for the simplicity of the person coding.

    The results using movie titles were:
     11244Collisions
     55738 Empty Spots
     0.10 Seconds used
    The results using movie quotes were:
     12277 Collisions
     4344707 Empty Spots
     0.16 Seconds used

Method 3 - In my third attempt to optimize my hash table I decided that I would change
    the hashing function in order to try and decrease the amount of space taken up
    which was a big issue in methods 1 and 2. In order to do this I attempted the 
    floor division method for my hashing function, this means that after all the ascii
    values were summed up I divided that number by a prime number(7) in the hopes of 
    lowering the highest index. Due to the fact that an index has to be a whole number
    it was important that I use floor division to remove any decimal places that may be
    present. I continued with the linked list method of collision handling in the hopes
    that my collisions and timing would stay low. With this addition there was a clear
    change in both the movie title and movie quote tables of the empty spot count being
    much lower that in the original attempts.There was almost no change in the amount
    of time required of the program which is good but suprisingly the number of 
    collisions increased again due to the table as a whole getting smaller. Overall so 
    far this method has had the most optimized numbers for memory required and timing
    but the issues with collisions are still present and the number of unused spots is
    still larger than ideal.

    The results using the movie titles were:
    Collisions: 14090
    Empty Spots: 7580
    Time used: 0.11 Seconds
    The results using the movie quotes were:
    Collisions: 14488
    Empty Spots: 620550
    Time used: 0.16 Seconds

Method 4 - Moving on to my fourth attempt I aimed to lower the amount of unused memory
    being created but wanted to keep some of the improvements that were found in the
    third method. By reverting back to the linear probing method but using the same 
    floor division technique I hoped to only use the space required of the size of the
    data. Although this attempt did a relatively poor job of upholding the advancements
    of the last few methods especially in my results of movie titles the amount of
    empty spots did decrease by a sizeable amount. The downfalls of this method mirror
    the issues that arose with using linear probing the previous times in that it
    creates a lot of collisions, uses much more time than linked list method and would
    be less than ideal if anyone ever needed to search for the data in the table. If 
    there was an extremely tight memory requirement then this method could be utilized
    but even still there are better ways to fulfill that need.

    The results using the movie titles were:
    Collisions: 14730
    Empty Spots: 8
    Time used: 6.50 Seconds
    The results using the movie quotes were:
    Collisions: 14795
    Empty Spots: 60606
    Time used: 6.51Seconds

Method 5 - Lastly in my final optimization attempt I hope to create a new hashing 
    function that created less duplicate values, reducing collisions, that kept
    the time required low, and that lowered the amount of unused space in memory.
    My new hashing function took the sum of the ascii values like the other 
    methods and then squared the sum and converted it into a string, then after 
    figuring out the length of the string I cut the first fourth and the last 
    fourth out and reconverted the middle half back into an integer. This method
    was called the mid-square method and hoped to better distribute the numbers.
    In addition to the changes in my hash function I also modded the key by the 
    size of the list in order to prevent out of index issues and lower the amount
    of empty spots. When handling collisions I decided to go with the linked 
    list method due to the improvements in the time required. Overall the
    improvements I saw using this method were better than other attempts due to
    the combination of collisions being normal, although normal is
    quite high, empty spots being relatively low and time used still being pretty
    optimized for the amount of data. This method I would consider to be the
    most optimized out of all of the methods if the user does not have any
    specific areas that need to be kept in check, like tight memory space or
    extremely fast computing.

    The results using the movie titles were:
    Collisions: 13795
    Empty Spots: 8787
    Time used: 0.24 Seconds
    The results using the movie quotes were:
    Collisions: 13386
    Empty Spots: 8378
    Time used: 0.28 Seconds

Overall, there is definitley more optimization that could still happen in 
order to add on to the improvements in method 5 but because of the
distinct issues that are present in any of the other attempts it
still is the most optimized for the hash table implementation. If I 
were to continue this project with more methods I would try using the
floor division method together with the mid-square method in order
to continue trying to reduce the number of unused spots
