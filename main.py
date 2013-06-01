#!/usr/bin/env python

# Evernote + python = FRIENDSHIP
# Brett Kelly — bkelly@evernote.com

import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.notestore.ttypes as NoteStoreTypes
import evernote.edam.type.ttypes as Types

from evernote.api.client import EvernoteClient

def getNonEmptyUserInput(prompt):
	"Prompt the user for input, disallowing empty responses"
	uinput = raw_input(prompt)
	if uinput:
		return uinput
	print "This can't be empty. Try again."
	return getNonEmptyUserInput(prompt)

auth_token = "" # set this to your dev token to avoid being prompted

if not auth_token:
    auth_token = getNonEmptyUserInput("Enter your developer token: ")

# Init EvernoteClient object with dev token and host
client = EvernoteClient(token=auth_token, sandbox=True)

# Create UserStore instance
user_store = client.get_user_store()
# Create NoteStore instance
note_store = client.get_note_store()

### Cocked, locked and ready to rock.

# Retrieve User object
user = user_store.getUser()
print "Username: %s" % user.username
print "Name: %s" % user.name

raw_input("Type return to continue...")

# Create a Note and save it to Evernote
note = Types.Note()
note.title = "I'm a new note!"
note.content = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">
<en-note>Gosh, you're handsome!</en-note>
"""
note = note_store.createNote(note)
print "Note created: %s" % note.guid

raw_input("Type return to continue...")

# Search notes for whatever the user inputs
nFilter = NoteStoreTypes.NoteFilter()
nFilter.words = getNonEmptyUserInput("Search for: ")
resultSpec = NoteStoreTypes.NotesMetadataResultSpec()
resultSpec.includeTitle = True

searchResults = note_store.findNotesMetadata(nFilter, 0, 10, resultSpec)

if len(searchResults.notes):
    for note in searchResults.notes:
        print note.guid
        print note.title
else:
    print "No results, big fella."


