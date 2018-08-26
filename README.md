
The comparison calculator was built with python. It consists of a single function
called comparison which take the inputs and the name of the output file and then produces the
average errors.

My code doesn't really have a whole lot of dependencies, it's fairly simple
I store the data in a dictionary where the stock ID is the key, and then there is an array of arrays holding the actual and predicted price at each hour.

I don't do a whole lot of exception handling here, though I am aware that 
exception handling is important for dealing with real data, 


I wasn't able to pass the test, I got 1405/1437 correct. The unmatched are all off by 0.01. I thought maybe it was a rounding issue, but this doesn't seem to be the case, so I am quite perplexed, if you could explain what I am doing wrong I would greatly appreciate, though I understand I probably won't receive the interview.

Thank you

Max





