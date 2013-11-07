TEMPLATE = app
CONFIG += console
CONFIG -= qt

SOURCES += main.cpp

OTHER_FILES += \
    stokescd.ufl \
    stokescr.ufl \
    stokesth.ufl

LIBS += -ldolfin

HEADERS += \
    stokesProblem.h
