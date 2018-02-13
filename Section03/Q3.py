
## Q.3-1 to Q.3-3
years_list = [1995, 1996, 1997, 1998, 1989, 1990]

print( 'Answer of Q3-2\n', years_list[3] )
print( 'Answer of Q3-3\n', years_list[-1] )

## Q.3-4 to Q.3-7
things = ["mozzarella", "cinderella", "salmonella"]

things[1] = things[1].capitalize() ## You must substitute.
print( 'Answer of Q3-5\n', things )

things[0] = things[0].upper()
print( 'Answer of Q3-6\n', things )

del things[2]
# You can also select follwing code.
# things.remove( 'salmonella' )
# del things[-1]
print( 'Answer of Q3-7\n', things )

## Q.3-8 to Q.3-9
surprise = ["Groucho", "Chico", "Harpo"]

surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1] = surprise[-1].capitalize()
print( 'Answer of Q3-9\n', surprise[-1] )

## Q.3-10 to Q.3-14
e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
print( 'Answer of Q3-10\n', e2f )

print( 'Answer of Q3-11\n', e2f["walrus"] )

f2e = {}
for english, french in e2f.items():
    f2e[french] = english
print( 'Answer of Q3-12\n', f2e )

print( 'Answer of Q3-13\n', f2e["chien"] )

e2f_set = set(e2f.keys())
print( 'Answer of Q3-14\n', e2f_set )

## Q.3-15 to Q.3-18
life = {\
        'animals': {\
                    'cats': [\
                             'Henri', 'Grumpy', 'Lucy'\
                    ],\
                    'octopi': {}, 'emus': {} \
        },\
        'plants': {}, 'other': {} \
}
print( 'Answer of Q3-15\n', life )
print( 'Answer of Q3-16\n', list ( life.keys() ) )
print( 'Answer of Q3-17\n', list ( life['animals'].keys() ) ) 
print( 'Answer of Q3-18\n', life['animals']['cats'] )


