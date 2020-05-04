def res(dat):
    if(len(dat['dietLabels'])==0):
        return {"error":True}
    y=str(dat['dietLabels'])
    y=y[1:-1]
    x={}
    z={
        'calories':round(dat['calories'],1),
        'dietLabels':y,
    }
    x.update(z)
    nutriitems=(dat['totalNutrients']).keys()
    if('FAT' in nutriitems):
        z={
            'FATQ':round(dat['totalNutrients']['FAT']['quantity'],1),
            'FATU':dat['totalNutrients']['FAT']['unit'],
            'FATUP':round(dat['totalDaily']['FAT']['quantity'],0)
        }
   
        x.update(z)


    if('NA' in nutriitems):
        z={
            'Sodiumq':round(dat['totalNutrients']['NA']['quantity'],1),
            'Sodiumu':dat['totalNutrients']['NA']['unit'],
            'Sodiump':round(dat['totalDaily']['NA']['quantity'],0)
        }
   
        x.update(z)

    if('FASAT' in nutriitems):
        z={
            'FASATQ':round(dat['totalNutrients']['FASAT']['quantity'],1),
            'FASATU':dat['totalNutrients']['FASAT']['unit'],
            'FASATP':round(dat['totalDaily']['FASAT']['quantity'],0)
        }
        x.update(z)
    
    if('CHOCDF' in nutriitems):
        z={
            'CARBSQ':round(dat['totalNutrients']['CHOCDF']['quantity'],1),
            'CARBSU':dat['totalNutrients']['CHOCDF']['unit'],
            'CARBSP':round(dat['totalDaily']['NA']['quantity'],0)
        }
        x.update(z)


    if('FIBTG' in nutriitems):
        z={
            'Fiberq':round(dat['totalNutrients']['FIBTG']['quantity'],1),
            'Fiberu':dat['totalNutrients']['FIBTG']['unit'],
            'Fiberp':round(dat['totalDaily']['FIBTG']['quantity'],0)

        }
        x.update(z)
    

    if('PROCNT' in nutriitems):
        z={
            'PROCNTQ':round(dat['totalNutrients']['PROCNT']['quantity'],1),
            'PROCNTU':dat['totalNutrients']['PROCNT']['unit'],
        }
        x.update(z)
    
    if('CHOLE' in nutriitems):
        z={
            'Cholesterolq':round(dat['totalNutrients']['CHOLE']['quantity'],1),
            'Cholesterolu':dat['totalNutrients']['CHOLE']['unit'],
            'Cholesterolup':round(dat['totalDaily']['CHOLE']['quantity'],0),
            
        }
        x.update(z)
     
    if('CHOLE' in nutriitems):
        z={
            'Cholesterolq':round(dat['totalNutrients']['CHOLE']['quantity'],1),
            'Cholesterolu':dat['totalNutrients']['CHOLE']['unit'],
            'Cholesterolup':round(dat['totalDaily']['CHOLE']['quantity'],0),
            
        }
        x.update(z)
     
    if('VITD' in nutriitems):
        z={
            'vitdq':round(dat['totalNutrients']['VITD']['quantity'],1),
            'vitdu':dat['totalNutrients']['VITD']['unit'],
            'vitdp':round(dat['totalDaily']['VITD']['quantity'],0)
                
        }
        x.update(z)
     
    if('CA' in nutriitems):
        z={
            'calcq':round(dat['totalNutrients']['CA']['quantity'],1),
            'calcu':dat['totalNutrients']['CA']['unit'],
            'calcp':round(dat['totalDaily']['CA']['quantity'],0)

        }
        x.update(z)
     
    if('FE' in nutriitems):
        z={
            'ironq':round(dat['totalNutrients']['FE']['quantity'],1),
            'ironu':dat['totalNutrients']['FE']['unit'],
            'ironp':round(dat['totalDaily']['FE']['quantity'],0),
                
        }
        x.update(z)
     
    if('K' in nutriitems):
        z={
            'potp':round(dat['totalDaily']['K']['quantity'],0),
            'potq':round(dat['totalNutrients']['K']['quantity'],1),
            'potu':dat['totalNutrients']['K']['unit']
                
        }
        x.update(z)
                   
    return x