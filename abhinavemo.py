def of(greeting):

    def inner(sep):

        def innermost(gname):
            from emojis import emojis
            emojized =emojis.encode(greeting +":"+sep+":"+gname)
            print(emojized)
            
        return innermost
    return inner
#-----------------------
enggrt=of("welcome")
engtgrgrt=enggrt("lion")
engtgrgrt("Abhinav")