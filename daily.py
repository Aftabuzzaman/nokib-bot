from setup import config
if(config['archiveTalk']['status']):
    import archive
    archive.archive()
"""if(config["reduceImage"]['status']):
    import reduceImage
    reduceImage.reduceFUR()"""
if(config["goodArticle"]["status"]):
    import ga
    ga.manageGATalk()
    ga.manageGAR()
    if(config["goodArticle"]["manageNominee"]["status"]):
        ga.manageNominee()
if(config['auditEditathon']['status']):
    import editathon