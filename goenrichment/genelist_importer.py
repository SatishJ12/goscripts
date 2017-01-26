#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Pieter Moris
'''

import os


def importBackground(path):
    """
    Imports the background set of genes (uniprot AC).

    Parameters
    ----------
    path : str
        The path to the file.

    Returns
    -------
    set of str
        A set of background uniprot AC's.

    Notes: Gene lists should not contain a header. One gene per line.
    Possible improvement: check for file structure and allow headers, comma separated lists, etc.
    """
    with open(path, 'r') as inGenes:
        backgroundSet = set([line.rstrip() for line in inGenes][1:])
    print('Retrieved', len(backgroundSet),
          'background uniprot AC\'s from', path)
    return backgroundSet


def importSubset(path):
    """
    Imports the gene subset of interest (uniprot AC).

    Parameters
    ----------
    path : str
        The path to the file.

    Returns
    -------
    set of str
        A subset of uniprot ACs of interest.

    Notes: Gene lists should not contain a header. One gene per line.
    """
    with open(path, 'r') as inGenes:
        geneSubset = set([line.rstrip() for line in inGenes][1:])
    print('Retrieved', len(geneSubset), 'subset uniprot AC\'s from', path)
    return geneSubset


def isValidSubset(subset, background):
    if subset.issubset(background):
        return True
    else:
        print('WARNING! Subset contained genes not present in background list. Terminating program now.')
        exit()
