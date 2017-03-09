# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit

# Open netedit
neteditProcess, match = netedit.setupAndStart(neteditTestRoot, False)

# Rebuild network
netedit.rebuildNetwork()

# zoom in central node
netedit.zoomIn(match.getTarget().offset(325, 225), 10)

# go to inspect mode
netedit.inspectMode()

# inspect first crossing
netedit.leftClick(match, 250, 225)

# try to change ID (cannot be possible)
netedit.modifyAttribute(0, "dummyID")

# Change Edges adding a new edge
netedit.modifyAttribute(1, "3 7 1")

# rebuild network
netedit.rebuildNetwork()

# Change Edges with the same edges as another crossing (Duplicate
# crossings aren't allow)
netedit.modifyAttribute(1, "4 8")

# rebuild network
netedit.rebuildNetwork()

# Change Edges to a single edge
netedit.modifyAttribute(1, "3")

# rebuild network
netedit.rebuildNetwork()

# Change priority
netedit.modifyBoolAttribute(2)

# Change width with a non valid value 1
netedit.modifyAttribute(3, "dummyWidth")

# Change width with a non valid value 2
netedit.modifyAttribute(3, "-3")

# Change width with a valid value
netedit.modifyAttribute(3, "4")

# rebuild network
netedit.rebuildNetwork()

# Check undos
netedit.undo(match, 3)

# rebuild network
netedit.rebuildNetwork()

# Check redos
netedit.redo(match, 3)

# save newtork
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess, False, False)
