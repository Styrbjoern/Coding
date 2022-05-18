
    # Step 1: First, we import the necessary modules.
    
import streamlit as st
import pandas as pd
import numpy as np
from random import seed
from random import randint
st.title('Nonsense poetry generator')
st.caption("""Welcome to the Nonsense Poetry Generator, or NPG!
When you pick a type of poem from the box, the NPG creates a unique poem for you. Your poem might not make sense (at all!), but it can always be read out loud in the rhythm of the type of poem you chose. The NPG doesn't know a whole lot of different words yet, but it'll always do its best to come up with something that rhymes in the right places!
If you want to learn more about the different types of poems, click to expand the section below!""")

with st.expander("What are the types of poems?"):
     st.subheader('Couplet')
     st.write("""
         A couplet is a short poem made of two lines. It's the first type of poems NPG learned to write, and although it has come far since then, it still takes pride in its humble roots.
     """)
     st.subheader('Limerick')
     st.write("""
         A limerick is a poem with a complicated rhyming scheme: AABBA, where the B lines are shorter than the A lines. Typically there's a place name of some sort in a limerick, but the NPG is so focused on getting the rhythm right that it often forgets about that.
     """)
     st.subheader('Iambic Pentameter')
     st.write("""
         Each line in a Iambic Pentameter consists of five iambs - that is to say, there's stress on every other syllable. It's the meter that Shakespeare used. When you ask NPG to write one of these, it imagines shouting it from a stage to a confused audience.
     """)
     st.subheader('Iambic Octameter')
     st.write("""
         This one is just like the Iambic Pentameter, except it just kind of... forgets to stop. If you know the tune of Gilbert & Sullivan's 'Modern Major General Song', you can sing these poems to it!
     """)
     st.subheader('Haiku')
     st.write("""
         This is a poem made of three lines - the first has five syllable, the second has seven, and the last has five again. NPG thinks Haiku are a nice change because it doesn't have to come up with rhymes.
     """)

#GNU Sir Terry Pratchett
#GNU Vibeke Jensen
    
    # Step 2: We then define a library of schemes for the function.
    # Each scheme is generated from a selection of possible structures for each line.
    # As of this version, the program can generate five schemes:
    # Couplet, limerick, iambic pentameter, haiku and iambic pentameter.
    
        #SCHEME: COUPLET
        
        # All the schemes are generated the same way, so I'll just explain this first one.
        # The first part creates an empty list to store the structure in, then specifies a 'recipe',
        # and a list of options for each unique line in the scheme.
              
couplet = []
couplet_recipe = ['line1','linebreak','line1']
couplet_options1 = [['xX','xX','xX','xX',('R','xX',0)],['x','Xx','Xx','Xx','Xx',('R','X',0)],['x','X','xX','xX','xX','x',('R','X',0)],['xX','x','Xx','X','xX',('R','xX',0)],['xX','xX','x','Xx','X',('R','xX',0)],['x','X','xX','xX','x','X','x',('R','X',0)]]

        # This next part fills in the empty list with randomly chosen items from the list of options.

for lines in couplet_recipe:
        if lines == 'line1':
            couplet = couplet + couplet_options1[randint(0,5)]
        elif lines == 'linebreak':
            couplet.append('linebreak')

        #SCHEME: LIMERICK
        
limerick = []
limerick_recipe = ['line1','linebreak','line1','linebreak','line2','linebreak','line2','linebreak','line1']
limerick_options1 = [['xX','xxX',('R','xxX',0)],['x','X','x','xX',('R','xxX',0)],['x','Xxx','X',('R','xxX',0)],['xX','x','xX',('R','xxX',0)],['xX','xxX','x',('R','xX',0)],['xX','x','x','Xx',('R','xX',0)],['x','Xx','xX','x',('R','xX',0)],['x','X','x','x','X','x',('R','xX',0)]]
limerick_options2 = [['xX',('R','xxX',1)],['x','Xx',('R','xX',1)],['x','X',('R','xxX',1)],['xX','x',('R','xX',1)],['x','X','x','x',('R','X',1)]]

for lines in limerick_recipe:
        if lines == 'line1':
            limerick = limerick + limerick_options1[randint(0,7)]
        elif lines == 'line2':
            limerick = limerick + limerick_options2[randint(0,4)]
        elif lines == 'linebreak':
            limerick.append('linebreak')

        #SCHEME: IAMBIC PENTAMETER

iambicpentameter = []
iambicpentameter_recipe = ['line1','linebreak','line1','linebreak','line2','linebreak','line2','linebreak','line3','linebreak','line3','linebreak','line4','linebreak','line4']
iambicpentameter_options1 = [['xX','xX','xX','xX',('R','xX',0)],['x','Xx','Xx','Xx','Xx',('R','X',0)],['x','X','xX','xX','xX','x',('R','X',0)],['xX','x','Xx','X','xX',('R','xX',0)],['xX','xX','x','Xx','X',('R','xX',0)],['x','X','xX','xX','x','X','x',('R','X',0)]]
iambicpentameter_options2 = [['xX','xX','xX','xX',('R','xX',1)],['x','Xx','Xx','Xx','Xx',('R','X',1)],['x','X','xX','xX','xX','x',('R','X',1)],['xX','x','Xx','X','xX',('R','xX',1)],['xX','xX','x','Xx','X',('R','xX',1)],['x','X','xX','xX','x','X','x',('R','X',1)]]
iambicpentameter_options3 = [['xX','xX','xX','xX',('R','xX',2)],['x','Xx','Xx','Xx','Xx',('R','X',2)],['x','X','xX','xX','xX','x',('R','X',2)],['xX','x','Xx','X','xX',('R','xX',2)],['xX','xX','x','Xx','X',('R','xX',2)],['x','X','xX','xX','x','X','x',('R','X',2)]]
iambicpentameter_options4 = [['xX','xX','xX','xX',('R','xX',3)],['x','Xx','Xx','Xx','Xx',('R','X',3)],['x','X','xX','xX','xX','x',('R','X',3)],['xX','x','Xx','X','xX',('R','xX',3)],['xX','xX','x','Xx','X',('R','xX',3)],['x','X','xX','xX','x','X','x',('R','X',3)]]


for lines in iambicpentameter_recipe:
        if lines == 'line1':
            iambicpentameter = iambicpentameter + iambicpentameter_options1[randint(0,5)]
        elif lines == 'line2':
            iambicpentameter = iambicpentameter + iambicpentameter_options2[randint(0,5)]
        elif lines == 'line3':
            iambicpentameter = iambicpentameter + iambicpentameter_options3[randint(0,5)]
        elif lines == 'line4':
            iambicpentameter = iambicpentameter + iambicpentameter_options4[randint(0,5)]
        elif lines == 'linebreak':
            iambicpentameter.append('linebreak')
                    
shakespeare = iambicpentameter
        
        #SCHEME: HAIKU
    
haiku = []
haiku_recipe = ['line1','linebreak','line2','linebreak','line1']
haiku_options1 = [['xX','xxX'],['x','Xx','xX'],['x','X','xxX'],['xX','x','xX'],['x','X','x','x','X'],['xX','Xxx'],['X','xX','xX'],['Xxx','x','X']]
haiku_options2 = [['xX','xX','xX','x'],['x','Xx','Xx','Xx'],['Xxx','X','xxX'],['xxX','xX','xX'],['xX','X','x','xxX'],['X','X','X','X','X','X','X'],['Xxx','Xx','Xx']]

for lines in haiku_recipe:
        if lines == 'line1':
            haiku = haiku + haiku_options1[randint(0,7)]
        elif lines == 'line2':
            haiku = haiku + haiku_options2[randint(0,6)]
        elif lines == 'linebreak':
            haiku.append('linebreak')
        
        #SCHEME: IAMBIC OCTAMETER ('MODERN MAJOR GENERAL')

iambicoctameter = []
iambicoctameter_recipe = ['line1','linebreak','line1','linebreak','line2','linebreak','line2']
iambicoctameter_options1 = [['xX','xX','xX','xX','xX','xX','xX',('R','xX',0)],['x','Xx','Xx','Xx','Xx','Xx','Xx','Xx',('R','X',0)],['x','X','x','X','xX','xX','x','X','xX','xX','x',('R','X',0)],['xX','xX','x','X','x','Xx','X','xX','xX',('R','xX',0)],['xX','xX','xX','x','Xx','X','x','X','xX',('R','xX',0)],['x','Xx','X','x','X','xX','xX','x','X','x','X','x',('R','X',0)]]
iambicoctameter_options2 = [['xX','xX','xX','xX','xX','xX','xX',('R','xX',1)],['x','Xx','Xx','Xx','Xx','Xx','Xx','Xx',('R','X',1)],['x','X','x','X','xX','xX','x','X','xX','xX','x',('R','X',1)],['xX','xX','x','X','x','Xx','X','xX','xX',('R','xX',1)],['xX','xX','xX','x','Xx','X','x','X','xX',('R','xX',1)],['x','Xx','X','x','X','xX','xX','x','X','x','X','x',('R','X',1)]]

for lines in iambicoctameter_recipe:
        if lines == 'line1':
            iambicoctameter = iambicoctameter + iambicoctameter_options1[randint(0,5)]
        elif lines == 'line2':
            iambicoctameter = iambicoctameter + iambicoctameter_options2[randint(0,5)]
        elif lines == 'linebreak':
            iambicoctameter.append('linebreak')
        
modernmajorgeneral = iambicoctameter        
        
        
    # Step 3: Now let's give the function a rhyming dictionary
    # The structure of each entry is a tuple containing:
    # The word [0], the syllable structure [1], and the rhyming class [2]
    
rhymedict = [('round ','X','ound'),('bound ','X','ound'),('sound ','X','ound'),('astound ','xX','ound'),('profound ','xX','ound'),('turnaround ','xxX','ound'),('turnaround ','Xxx','ound'),('underground ','xxX','ound'),('underground ','Xxx','ound'),('abound ','xX','ound'),('compound ','xX','ound'),('around ','xX','ound'),
             ('blue ','X','oo'),('true ','X','oo'),('due ','X','oo'),('cue ','X','oo'),('stew ','X','oo'),('new ','X','oo'),('subdue ','xX','oo'),('flew ','X','oo'),('chew ','X','oo'),('achoo! ','xX','oo'),('to ','x','oo'),('too ','x','oo'),('two ','x','oo'),('two ','X','oo'),('Peru ','xX','oo'),
             ('hop ','X','op'),('stop ','X','op'),('drop ','X','op'),('scallop ','Xx','op'), ('gallop ','Xx','op'),('ketchup ','Xx','op'),
             ('of ','x','off'),('rough ','X','off'),('enough ','xX','off'),('tough ','X','off'),('love ','X','off'),('turtledove ','xxX','off'),('turtledove ','Xxx','off'),
             ('the ','x','ee'),('be ','X','ee'),('be ','x','ee'),('jubee! ','xX','ee'),('jubilee ','xxX','ee'),("Maitre d' ",'xxX','ee'),('recipe ','Xxx','ee'),('Odyssey ','xxX','ee'),('see ','X','ee'),('we ','x','ee'),('tree ','X','ee'),('flee ','X','ee'),('Cree ','X','ee'),('plea ','X','ee'),
             ('that ','X','at'),('hat ','X','at'),('rat ','X','at'),('that ','x','at'),('mat ','X','at'),('cat ','X','at'),('flat ','X','at'),('matte ','X','at'),('egad! ','xX','at'),('chat ','X','at'),('iron-clad ','xxX','at'),('babysat ','xxX','at'),
             ('understand ','xxX','and'),('contraband ','Xxx','and'),('contraband ','xxX','and'),('stand ','X','and'),('land ','X','and'), ('land ','x','and'),('command ','xX','and'),('expand ','xX','and'),('firsthand ','xX','and'),('demand ','xX','and'),('withstand ','xX','and'),('and ','X','and'),('and ','x','and'),('hand ','X','and'),('ampersand ','xxX','and'),
             ('contradict ','xxX','ict'),('evict ','xX','ict'),('depict ','xX','ict'),('clicked ','X','ict'),('flicked ','X','ict'),('tricked ','X','ict'),
             ('engineer ','xxX','eer'),('commandeer ','xxX','eer'),('steer ','X','eer'),('hear ','X','eer'),('hear ','x','eer'),('ear ','X','eer'),("we're ",'x','eer'),('here ','X','eer'),('here ','x','eer'),('veneer ','xX','eer'),('buccaneer ','xxX','eer'),('volunteer ','xxX','eer'),('musketeer ','xxX','eer'),('brigadier ','xxX','eer'),('appear ','xX','eer'),
             ('anapest ','xxX','est'),('Budapest ','xxX','est'),('manifest ','xxX','est'),('arrest ','xX','est'),('west ','X','est'),('test ','X','est'),('best ','X','est'),('rest ','X','est'),('attest ','xX','est'),
             ('dance ','X','ance'),('prance ','X','ance'),('stance ','X','ance'),('finance ','xX','ance',),('vans ','X','ance'),('romance ','xX','ance'),('plans ','X','ance'),('enhance ','xX','ance'),('chance ','X','ance'),('countenance ','xxX','ance'),('countenance ','Xxx','ance'),('France ','X','ance'),
             ('not ','x','ot'),('hot ','x','ot'),('what ','X','ot'),('plot ','X','ot'),('ballot ','Xx','ot'),('rot ','X','ot'),('lot ','X','ot'),('robot ','Xx','ot'),('carrot ','Xx','ot'),('allot ','xX','ot'),('cannot ','Xx','ot'),('cannot ','xX','ot'),('parrot ','Xx','ot'),('shot ','X','ot'),
             ('a ','x','a'),('a ','x','a'),
             ('on ','x','on'),
             ('if ','x','if'),
             ('in ','x','in'),
             ('this ','x','is'),('is ','x','is'),('is ','x','is'),
             ('was ','x','us'),('us ','x','us'),
             ('there ','x','ehr'),
             ('young ','x','ung'),
             ('from ','x','omm'),
             ('content ','Xx','ent'),('content ','xX','ent'),('circumvent ','xxX','ent'),('president ','Xxx','ent'),('precedent ','Xxx','ent'),('vent ','X','ent'),('sent ','X','ent'),('meant ','X','ent'),('invent ' ,'xX','ent'),('intent ','xX','ent'),('tent ','X','ent'),('repent ','xX','ent'),('decent ','Xx','ent'),('descent ','xX','ent'),('scent ','X','ent'),('supplement ','Xxx','ent'),('supplement ','xxX','ent'),('infrequent ','xxX','ent'),('frequent ','Xx','ent'),('lament ','xX','ent'),
             ('ate ','X','aid'),('berate ','xX','aid'),('contemplate ','Xxx','aid'),('contemplate ','xxX','aid'),('concentrate ','Xxx','aid'),('concentrate ','xxX','aid'),('navigate ','Xxx','aid'),('navigate ','xxX','aid'),('allocate ','Xxx','aid'),('allocate ','xxX','aid'),('late ','X','aid'),('state ','X','aid'),('rate ','X','aid'),('inflate ','xX','aid'),('made ','X','aid'),('forbade ','xX','aid'),('instigate ','Xxx','aid'),('instigate ','xxX','aid'),('surrogate ','Xxx','aid'),('glade ','X','aid'),('reinstate ','xxX','aid'),('instate ','xX','aid'),('laminate ','Xxx','aid'),('laminate ','xxX','aid'),('sedate ','xX','aid'),('parade ','xX','aid'),('aid ','X','aid'),('portrayed ','xX','aid'),('plate ','X','aid'),('front-gate ','Xx','aid'),('delayed ','xX','aid'),('man-made ','Xx','aid'),('date ','X','aid'),('conflate ','xX','aid'),('evade ','xX','aid'),
             ('shirt ','X','erd'),('absurd ','xX','erd'),('overheard ','xxX','erd'),('outskirt '),('dessert ','xX','erd'),('flirt ','X','erd'),('stirred ','X','erd'),('undeterred ','xxX','erd'),
             ('wear ','X','air'),('hair ','X','air'),('where ','X','air'),('where ','x','air'),('bear ','X','air'),('stare ', 'X', 'air'),('flare ','X','air'),('compare ','xX','air'),('au contraire ','xxX','air'),('millionaire ','Xxx','air'),('millionaire ','xxX','air'),('repair ','xX','air'),('despair ','xX','air'),('chair ','X','air'),('rare ','X','air'),('air ','X','air'),('aware ','xX','air'),('declare ','xX','air'),('nightmare ','Xx','air'),('blare ','X','air'),('share ','X','air'),('spare ','X','air'),('aware ','xX','air'),('unaware ','Xxx','air'),('unaware ','xxX','air'),('underwear ','Xxx','air'),
             ('interact ','xxX','act'),('counteract ','Xxx','act'),('compact ','Xx','act'),('compact ','xX','act'),('distract ','xX','act'),('detract ','xX','act'),('whacked ','X','act'),('stacked ','X','act'),('unpacked ','xX','act'),('quacked ','X','act'),('snacked ','X','act'),('dragged ','X','act'),('packed ','X','act'),('fact ','X','act'),('contact ','Xx','act'),('contract ','Xx','act'),('enact ','xX','act'),('exact ','xX','act'),('inexact ','xxX','act'), ('extract ','xX','act'),
            ]

#correspond,pond,
#your,tour,sure,puncture,assure,reassure,demure,
#now,how,vow,ow!,
#big,trick,flick,stick, 
#win,spin,thin,kin,sin,tin,bin,
#sweet,street,meet,treat,beat,neat,
#man
#lad


        # Step 4: Now, we go on to define the main function.
        # We start by creating an empty string, where we will store the poem,
        # an empty list, which will help us keep track of the rhymes,
        # and another empty list, which will help us to prevent words rhyming with themselves.

def poemwriter(scheme=couplet):

        poem = ''
        rhymes = []
        rhymewords = []
        
        for word in scheme:
    
            # If the scheme requires a line break, we represent that with a slash.
        
            if word == 'linebreak':
                poem = poem + ' / '
            
            # Next, let's account for words that don't have to rhyme.
            # These only need to match the syllable/stress pattern, so we make a list of words that match,
            # and pick a random entry from that list.
            
            elif 'R' not in word:
                options = []
                for entry in rhymedict:
                    if entry[1] == word:
                        options.append(entry)
                top = len(options)
                if top == 0:
                    poem = poem + word
                else:
                    rand_int = randint(0,top)
                    chosen_option = options[rand_int-1]
                    poem = poem + chosen_option[0]
            
            # If the word does need to rhyme, we do the same, but we then add an entry to the list of rhymes.
            # This entry helps the function remember how the word sounds,
            # and can be retrieved when we need a word to rhyme with it later.
            # That's what's happening in the 'else' clause here.
            # The three 'if' clauses of descending complexity, inside the 'else' clause,
            # ensure that the function will only rhyme a word with itself
            # if it can't find any other words that fit the meter.
            
            elif 'R' in word:
                if len(rhymes) <= word[2]:
                    options = []
                    for entry in rhymedict:
                        if entry[1] == word[1]:
                            options.append(entry)
                    top = len(options)
                    if top == 0:
                        poem = poem + word[1]
                    else:
                        rand_int = randint(0,top)
                        chosen_option = options[rand_int-1]
                        poem = poem + chosen_option[0]
                        rhymes.append(chosen_option[2])
                        rhymewords.append(chosen_option[0])
                else:
                    options = []
                    for entry in rhymedict:
                        if entry[1] == word[1] and entry[2] == rhymes[word[2]] and entry[0] not in rhymewords:
                            options.append(entry)
                    top = len(options)
                    if top == 0:
                        for entry in rhymedict:
                            if entry[1] == word[1] and entry[2] == rhymes[word[2]]:
                                options.append(entry)
                    top = len(options)
                    if top == 0:
                        for entry in rhymedict:
                            if entry[1] == word[1]:
                                options.append(entry)
                    rand_int = randint(0,top)
                    chosen_option = options[rand_int-1]
                    poem = poem + chosen_option[0]
                    rhymewords.append(chosen_option[0])
            
    # Step 5: Finally, let's ask the function to print the finished poem
        return poem[:-1]
    

#Additions made for the Streamlit application:
    
Chosen_scheme = st.selectbox(
     'Which kind of poem do you want to hear?',
     ('Pick a poem','Couplet', 'Limerick', 'Iambic Pentameter','Iambic Octameter','Haiku'))
    
if Chosen_scheme == 'Couplet':
    st.write(poemwriter(couplet))
elif Chosen_scheme == 'Limerick':
    st.write(poemwriter(limerick))
elif Chosen_scheme == 'Iambic Pentameter':
    st.write(poemwriter(iambicpentameter))
elif Chosen_scheme == 'Iambic Octameter':
    st.write(poemwriter(iambicoctameter))
elif Chosen_scheme == 'Haiku':
    st.write(poemwriter(haiku))
elif Chosen_scheme == 'Pick a poem':
    st.write('This is where your poem will appear.')
    
    
