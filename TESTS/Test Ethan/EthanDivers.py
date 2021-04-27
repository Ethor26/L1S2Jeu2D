# PersoPion.move(img_Vaisseau,self.PosX,self.PosY)
#
#
# img_Vaisseau = PhotoImage(file="IMAGES/faucon millenium-3.png")
#         CanevasJeu.create_image(self.PosX, self.PosY, anchor=NW, image=img_Vaisseau)
#         img_Vaisseau.zoom(1,1)
#
# # on passe le voleur au premier plan
# self.CanevasJeu.tag_raise(img_Vaisseau, ALL)

# Inutilisés : programmation collisions
# i['dx'] = -i['dx']
# CopieObjBall = self.balls[j]
# CopieCoordBall = self.balles[j]
# Modif de balls, balles et des coordonnées de départ à faire
# self.CanevasJeu.delete(self.balls[j])

# di['dy'] = -i['dy']
# Collision entre les balles
# ordre = 1/2, 1/3, 1/4, 2/3, 2/4, 3/4
#         for i in range(len(self.balles)):
#             j = i + 1
#             while j < len(self.balles):
#                 # Test si (ray1+ray2)² > dist(x1-x2)² + dist(y1-y2)²
#                 # et interverti les dx et dy
#                 if (self.balles[i]['ray'] + self.balles[j]['ray']) ** 2 > \
#                         ((self.balles[i]['x'] - self.balles[j]['x']) ** 2 +  # \
#                          (self.balles[i]['y'] - self.balles[j]['y']) ** 2):
#                     self.balles[i]['dx'], self.balles[j]['dx'] = self.balles[j]['dx'], self.balles[i]['dx']
#                     self.balles[i]['dy'], self.balles[j]['dy'] = self.balles[j]['dy'], self.balles[i]['dy']
#                  j += 1

# Autre methode pour modifier un texte sans stringVar:
# self.compteur_lbl.configure(text=str(int(self.CompteurScore)))
# self.compteur_lbl['text'] = str(int(self.CompteurScore))