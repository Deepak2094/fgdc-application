""" This code File automates the Meta Data Update Process FOR MULTIPLE FILES"""

# Importing Required Modules
import xml.etree.ElementTree as ET
from datetime import date
import os


def FGDC_Meta_Data_Automation(data):
    # Input and Output Path Declaration
    directoryPath = data['Folder_Path']
    folderList = []
    fileList = []
    OutputFileList = []

    for dirpath, dirnames, filenames in os.walk(directoryPath):
        for dirnames in dirnames:
            folderList.append(dirnames)

    for item in folderList:
        for file in os.listdir(directoryPath + "/" + item):
            if file.endswith(".xml"):
                tempFileName = os.path.join(directoryPath + "/" + item, file)
                fileList.append(tempFileName)
                tempOutFileName = os.path.join(directoryPath + "/" + item, "Updated" + "_" + file)
                OutputFileList.append(tempOutFileName)

    # --------------------- Declaring Variables to be Updated in respective Tabs ---------------------

    # Tab 1. Identification Info
    county = data['county_city']  # Specify the County or City for which the Meta data is being updated
    StateAbb = data['StateAbb']  # State Abbreviation
    StateFF = data['StateFF']  # State Full form
    Year = data['Year']  # Year in which the Meta Data was created/Updated
    CD_Obtained_Date = data['CD_Obtained_Date']  # The year in which the Dataset was copied from the CD

    pubdate = Year
    ID_Originator = data['ID_Originator']  # Organisation/Person responsible for creating dataset
    ID_title = "Enter Title here" + "," + " " + county + "," + " " + StateAbb + " " + Year
    ID_accconst = data['ID_accconst']
    ID_abstract = "This dataset represents the  "     "in" + " " + county + "," + " " + StateAbb + " " + Year
    ID_purpose = data['ID_purpose']
    ID_useconst = data['ID_useconst']

    # Contact Info
    ID_cntorg = data['ID_cntorg']
    ID_cntper = data['ID_cntper']
    ID_cntpos = data['ID_cntpos']
    ID_cntvoice = data['ID_cntvoice']
    ID_addrtype = data['ID_addrtype']
    ID_address = data['ID_address']
    ID_city = data['ID_city']
    ID_state = data['ID_state']
    ID_postal = data['ID_postal']
    ID_cntemail = data['ID_cntemail']

    # Theme Keywords
    MainKeyword = "Recreation"
    Keyword1 = "Parks"
    Keyword2 = "Public"

    # Tab 2.Data Quality
    DQ_attraccr = data['DQ_attraccr']
    DQ_logic = data['DQ_logic']
    DQ_complete = data['DQ_complete']
    DQ_horizpar = data['DQ_horizpar']
    DQ_vertaccr = data['DQ_vertaccr']
    DQ_procdesc = "Dataset copied from the cd obtained from" + " " + county + "," + " " + StateAbb + " " + CD_Obtained_Date
    DQ_procdate = data['DQ_procdate']

    # Tab 3 and 4 Have to be updated Manually

    # Tab 5. Distribution Info
    # For Tab 5 the duplicate Variables are not declared here; rather it is declared in Tab 6 below
    DI_distliab = data['DI_distliab']
    DI_fees = data['DI_fees']

    # Tab 6. Meta Info
    MI_cntorg = data['MI_cntorg']
    MI_cntper = data['MI_cntper']
    MI_cntvoice = data['MI_cntvoice']
    MI_cntemail = data['MI_cntemail']
    MI_addrtype = data['MI_addrtype']
    MI_address = data['MI_address']
    MI_city = data['MI_city']
    MI_state = data['MI_state']
    MI_postal = data['MI_postal']
    MI_metstdn = data['MI_metstdn']
    MI_metstdv = data['MI_metstdv']
    print(MI_cntorg)

    today = date.today()  # Getting Current Date
    Date = today.strftime("%Y%m%d")  # Converting Date time to string in Y-m-d format
    MI_metd = Date  # Assinging the current date to variables

    # --------------------------- Main Code Starts here   ---------------------------

    def metadataupdate(root, tree, count):
        # Tab 1:Identification Info
        if tree.find('idinfo/citation/citeinfo/title') is not None:
            title = tree.find('idinfo/citation/citeinfo/title').text
            if title is None:
                tree.find('idinfo/citation/citeinfo/title').text = ID_title
            elif title.lower().find("required", 0,
                                    12) > -1:  # if the value conatins required in file it will be updated
                tree.find('idinfo/citation/citeinfo/title').text = ID_title
            else:
                tree.find(
                    'idinfo/citation/citeinfo/title').text = title + "," + " " + county + "," + " " + StateAbb + " " + Year

        if tree.find('idinfo/citation/citeinfo/origin') is not None:
            origin = tree.find('idinfo/citation/citeinfo/origin').text
            if origin is None:
                tree.find('idinfo/citation/citeinfo/origin').text = ID_Originator
            elif origin.lower().find("required", 0, 12) > -1 or origin.lower().find("n/a", 0, 12) > -1:
                tree.find('idinfo/citation/citeinfo/origin').text = ID_Originator

        if tree.find('idinfo/accconst') is not None:
            acccnst = tree.find('idinfo/accconst').text
            if acccnst is None:
                tree.find('idinfo/accconst').text = ID_accconst
            elif acccnst.lower().find("required", 0, 12) > -1 or acccnst.lower().find("n/a", 0, 12) > -1:
                tree.find('idinfo/accconst').text = ID_accconst

        if tree.find('idinfo/useconst') is not None:
            usecnst = tree.find('idinfo/useconst').text
            if usecnst is None:
                tree.find('idinfo/useconst').text = ID_useconst
            elif usecnst.lower().find("required", 0, 12) > -1 or usecnst.lower().find("n/a", 0, 12) > -1:
                tree.find('idinfo/useconst').text = ID_useconst

        if tree.find('idinfo/citation/citeinfo/pubdate') is not None:
            pudate = tree.find('idinfo/citation/citeinfo/pubdate').text
            if pudate is None:
                tree.find('idinfo/citation/citeinfo/pubdate').text = pubdate
            elif pudate.lower().find("required", 0, 12) > -1 or pudate.lower().find("n/a", 0, 12) > -1:
                tree.find('idinfo/citation/citeinfo/pubdate').text = pubdate

        if tree.find('idinfo/descript/abstract') is not None:
            abst = tree.find('idinfo/descript/abstract').text
            if abst is None:
                tree.find('idinfo/descript/abstract').text = ID_abstract
            elif abst.lower().find("required", 0, 12) > -1 or abst.lower().find("n/a", 0, 12) > -1:
                tree.find('idinfo/descript/abstract').text = ID_abstract

        if tree.find('idinfo/descript/purpose') is not None:
            purpose = tree.find('idinfo/descript/purpose').text
            if purpose is None:
                tree.find('idinfo/descript/purpose').text = ID_purpose
            elif purpose.lower().find("required", 0, 12) > -1 or purpose.lower().find("n/a", 0, 12) > -1:
                tree.find('idinfo/descript/purpose').text = ID_purpose

        idinfo = tree.find('idinfo')
        if idinfo is not None:
            for child in list(idinfo):
                if child.tag == 'ptcontac':
                    idinfo.remove(child)

            ptcontac = ET.SubElement(idinfo, 'ptcontac')
            cntinfo = ET.SubElement(ptcontac, 'cntinfo')
            cntorgp = ET.SubElement(cntinfo, 'cntorgp')
            cntorg = ET.SubElement(cntorgp, 'cntorg')
            cntper = ET.SubElement(cntorgp, 'cntper')
            cntorg.text = ID_cntorg
            cntper.text = ID_cntper
            cntpos = ET.SubElement(cntinfo, 'cntpos')
            cntpos.text = ID_cntpos
            cntaddr = ET.SubElement(cntinfo, 'cntaddr')
            addrtype = ET.SubElement(cntinfo, 'addrtype')
            address = ET.SubElement(cntinfo, 'address')
            city = ET.SubElement(cntinfo, 'city')
            state = ET.SubElement(cntinfo, 'state')
            postal = ET.SubElement(cntinfo, 'postal')
            addrtype.text = ID_addrtype
            address.text = ID_address
            city.text = ID_city
            state.text = ID_state
            postal.text = ID_postal
            cntvoice = ET.SubElement(cntinfo, 'cntvoice')
            cntvoice.text = ID_cntvoice
            cntemail = ET.SubElement(cntinfo, 'cntemail')
            cntemail.text = ID_cntemail

        kw = tree.find('idinfo/keywords')
        if kw is not None:
            for child in list(kw):
                if child.tag == 'place':
                    kw.remove(child)

            place = ET.SubElement(kw, 'place')
            placekt = ET.SubElement(place, 'placekt')
            placekt.text = county + "," + " " + StateAbb
            placekey = ET.SubElement(place, 'placekey')
            placekey.text = StateFF
            placekey = ET.SubElement(place, 'placekey')
            placekey.text = StateAbb

        # Tab 2: Data Quality
        if tree.find('dataqual/attracc/attraccr') is not None:
            attr = tree.find('dataqual/attracc/attraccr').text
            if attr is None:
                tree.find('dataqual/attracc/attraccr').text = DQ_attraccr
            elif attr.lower().find("required", 0, 12) > -1 or attr.lower().find("n/a", 0, 12) > -1:
                tree.find('dataqual/attracc/attraccr').text = DQ_attraccr

        if tree.find('dataqual/logic') is not None:
            logc = tree.find('dataqual/logic').text
            if logc is None:
                tree.find('dataqual/logic').text = DQ_logic
            elif logc.lower().find("required", 0, 12) > -1 or logc.lower().find("n/a", 0, 12) > -1:
                tree.find('dataqual/logic').text = DQ_logic

        if tree.find('dataqual/complete') is not None:
            compt = tree.find('dataqual/complete').text
            if compt is None:
                tree.find('dataqual/complete').text = DQ_complete
            elif compt.lower().find("required", 0, 12) > -1 or compt.lower().find("n/a", 0, 12) > -1:
                tree.find('dataqual/complete').text = DQ_complete

        if tree.find('dataqual/lineage/procstep/procdate') is not None:
            prdate = tree.find('dataqual/lineage/procstep/procdate').text
            if prdate is None:
                tree.find('dataqual/lineage/procstep/procdate').text = DQ_procdate
            elif prdate.lower().find("required", 0, 12) > -1 or prdate.lower().find("n/a", 0, 12) > -1:
                tree.find('dataqual/lineage/procstep/procdate').text = DQ_procdate

        if tree.find('dataqual/lineage/procstep/procdesc') is not None:
            prdsc = tree.find('dataqual/lineage/procstep/procdesc').text
            if prdsc is None:
                tree.find('dataqual/lineage/procstep/procdesc').text = DQ_procdesc
            elif prdsc.lower().find("required", 0, 12) > -1 or prdsc.lower().find("n/a", 0, 12) > -1:
                tree.find('dataqual/lineage/procstep/procdesc').text = DQ_procdesc

        if tree.find('dataqual/posacc/horizpa/horizpar') is not None:
            horz = tree.find('dataqual/posacc/horizpa/horizpar').text
            if horz is None:
                tree.find('dataqual/posacc/horizpa/horizpar').text = DQ_horizpar
            elif horz.lower().find("required", 0, 12) > -1 or horz.lower().find("n/a", 0, 12) > -1:
                tree.find('dataqual/posacc/horizpa/horizpar').text = DQ_horizpar

        if tree.find('dataqual/posacc/vertacc/vertaccr') is not None:
            vert = tree.find('dataqual/posacc/vertacc/vertaccr').text
            if vert is None:
                tree.find('dataqual/posacc/vertacc/vertaccr').text = DQ_vertaccr
            elif vert.lower().find("required", 0, 12) > -1 or vert.lower().find("n/a", 0, 12) > -1:
                tree.find('dataqual/posacc/vertacc/vertaccr').text = DQ_vertaccr

        # Tab 5. Distribution info
        distributioninfo = root.find('distinfo')
        if root.find('distinfo') is not None:
            root.remove(distributioninfo)

        distinfo = ET.Element("distinfo")
        distrib = ET.SubElement(distinfo, 'distrib')
        cntinfo = ET.SubElement(distrib, 'cntinfo')
        cntorgp = ET.SubElement(cntinfo, 'cntorgp')
        cntorg = ET.SubElement(cntorgp, 'cntorg')
        cntper = ET.SubElement(cntorgp, 'cntper')
        cntorg.text = MI_cntorg
        cntper.text = MI_cntper
        cntaddr = ET.SubElement(cntinfo, 'cntaddr')
        addrtype = ET.SubElement(cntinfo, 'addrtype')
        address = ET.SubElement(cntinfo, 'address')
        city = ET.SubElement(cntinfo, 'city')
        state = ET.SubElement(cntinfo, 'state')
        postal = ET.SubElement(cntinfo, 'postal')
        addrtype.text = MI_addrtype
        address.text = MI_address
        city.text = MI_city
        state.text = MI_state
        postal.text = MI_postal
        cntvoice = ET.SubElement(cntinfo, 'cntvoice')
        cntvoice.text = MI_cntvoice
        cntemail = ET.SubElement(cntinfo, 'cntemail')
        cntemail.text = MI_cntemail
        distliab = ET.SubElement(distinfo, 'distliab')
        distliab.text = DI_distliab
        stdorder = ET.SubElement(distinfo, 'stdorder')
        digform = ET.SubElement(stdorder, 'digform')
        digtinfo = ET.SubElement(digform, 'digform')
        formname = ET.SubElement(digtinfo, 'formname')
        formname.text = "Digital Data"
        digtopt = ET.SubElement(digform, 'digtopt')
        onlinopt = ET.SubElement(digtopt, 'onlinopt')
        computer = ET.SubElement(onlinopt, 'computer')
        networka = ET.SubElement(computer, 'networka')
        networkr = ET.SubElement(networka, 'networkr')
        fees = ET.SubElement(stdorder, 'fees')
        fees.text = DI_fees
        resdesc = ET.SubElement(distinfo, 'resdesc')
        resdesc.text = "Downloadable Data"
        resdesc.set('Sync', "TRUE")

        root.append(distinfo)

        # Tab 6 : Meta Data Info Update
        metadatainfo = root.find('metainfo')
        if root.find('metainfo') is not None:
            root.remove(metadatainfo)

        metainfo = ET.Element("metainfo")
        metd = ET.SubElement(metainfo, 'metd')
        metd.text = MI_metd
        metc = ET.SubElement(metainfo, 'metc')
        cntinfo = ET.SubElement(metc, 'cntinfo')
        cntorgp = ET.SubElement(cntinfo, 'cntorgp')
        cntorg = ET.SubElement(cntorgp, 'cntorg')
        cntper = ET.SubElement(cntorgp, 'cntper')
        cntorg.text = MI_cntorg
        cntper.text = MI_cntper
        cntaddr = ET.SubElement(cntinfo, 'cntaddr')
        addrtype = ET.SubElement(cntinfo, 'addrtype')
        address = ET.SubElement(cntinfo, 'address')
        city = ET.SubElement(cntinfo, 'city')
        state = ET.SubElement(cntinfo, 'state')
        postal = ET.SubElement(cntinfo, 'postal')
        addrtype.text = MI_addrtype
        address.text = MI_address
        city.text = MI_city
        state.text = MI_state
        postal.text = MI_postal
        cntvoice = ET.SubElement(cntinfo, 'cntvoice')
        cntvoice.text = MI_cntvoice
        cntemail = ET.SubElement(cntinfo, 'cntemail')
        cntemail.text = MI_cntemail
        metstdn = ET.SubElement(metainfo, 'metstdn')
        metstdn.text = MI_metstdn
        metstdv = ET.SubElement(metainfo, 'metstdv')
        metstdv.text = MI_metstdv
        mettc = ET.SubElement(metainfo, 'mettc')
        mettc.text = "local time"
        mettc.set('Sync', "TRUE")

        root.append(metainfo)

        tree.write(OutputFileList[count])

    count = 0
    for filename in fileList:
        tree = ET.parse(filename)
        root = tree.getroot()
        metadataupdate(root, tree, count)
        count = count + 1
