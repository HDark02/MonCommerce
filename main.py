from datetime import datetime
import os
from kivymd.uix.backdrop.backdrop import MDFloatLayout
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivy.lang import Builder
from kivy.core.window import Window
from plyer import filechooser
from kivymd.uix.card import MDCard
from kivymd.uix.list import OneLineListItem
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screenmanager import ScreenManager
# from kivy.uix.spinner import Spinner
# from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
# from kivy.uix.popup import Popup
from kivymd.toast.kivytoast.kivytoast import toast
Window.keyboard_anim_args ={'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"
from kivymd.uix.screenmanager import ScreenManager
import json
# from kivy.utils import platform
from pathlib import Path
import time
import webbrowser
# Window.keyboard_anim_args ={'d': .2, 't': 'in_out_expo'}
# Window.softinput_mode = "below_target"
# Window.size = (400, 840)
# Window._set_top(1)
# Window._set_left(1)

fichier_for_products = "produits.json"

################################################"
# import hashlib

# # Hash du mot de passe entrer par l'utilisateur 
# PASSWORD_HASH = hashlib.sha256("1234".encode()).hexdigest()

# def check_password(self, password):
#     hashed = hashlib.sha256(password.encode()).hexdigest()

#     if hashed == PASSWORD_HASH:
#         self.root.current = "home"
#     else:
#         self.root.get_screen("login").ids.message.text = "Mot de passe incorrect"
# # ###################################################""
class Enter_intput(MDTextField):
    pass
class Depense_histo(OneLineListItem):
    date= StringProperty()
    description= StringProperty()
    enter_categorie_categorie_enter= StringProperty()
    montant= StringProperty()
    pass
class Bord_card(MDFloatLayout):
    # title= StringProperty()
    # money= StringProperty()
    # money_color= StringProperty()
    # bor_color= "red"
    # icon_bord= StringProperty()
    # icon_bord_opacity= 1
    # rate_info= StringProperty()
    # rate_info_color= "black"
    pass
#################################StringProp)
class Line_histo(OneLineListItem):
    date= StringProperty()
    client= StringProperty()
    numero_du_client= StringProperty()
    montant= StringProperty()
    paiement= StringProperty()
    categorie= StringProperty()
    livraison= StringProperty()
    actions= StringProperty()
    pass
########################################
class Line_gestion(OneLineListItem):
    date= StringProperty()
    descrip= StringProperty()
    catego= StringProperty()
    montant= StringProperty()
    action= StringProperty()

    # action= StringProperty()
    # action1= StringProperty()
    pass
#########################################
class Rapport_action(MDFloatLayout):
    # produit_nbr_serie= StringProperty()
    # date= StringProperty()
    # prix= StringProperty()
    # client= StringProperty()
    # paye= StringProperty()
    # nbr_article=StringProperty()
    # action=StringProperty()
    pass
#####################################


class MonCommerce(MDApp):
    def on_start(self):
        if os.path.exists(fichier_for_products):
            ##################
            tableau_de_bord =screen_manager.get_screen("gestion_des_vente_home").navig.acceuil_id.tableau_de_bord_id
            tableau_de_bord.date_actuelle.text = f"Aperçu de l'activité du {datetime.now().strftime('%d/%m/%Y')}"
            
            ##################
            self.reload_tableau_de_bord()

            self.load_histo_des_ventes()
            self.load_histo_des_depenses()
            # screen_manager.transition.direction = "left"
            screen_manager.current = "gestion_des_vente_home"
        else:
            # screen_manager.current = "gestion_des_vente_home"
            produit_data={
                "produits_paye": [],
                "produits_impaye": [],
                "depense": []
                }
            with open(fichier_for_products, "w", encoding="utf-8") as file:
                json.dump(produit_data, file, indent=4, ensure_ascii=False)
        #Reload tableau de bord for actualisé
    def reload_tableau_de_bord(self):
        # try:
        vente_impaye_total=self.total_des_ventes_impayes()
        depense_total= self.total_des_depenses()
        vente_paye_total=self.total_des_ventes_payes()
        total_des_ventes=vente_impaye_total + vente_paye_total
        ##################
        tableau_de_bord =screen_manager.get_screen("gestion_des_vente_home").navig.acceuil_id.tableau_de_bord_id
        ##################
        tableau_de_bord.total_des_ventes.money= f"{total_des_ventes} F"
        tableau_de_bord.payement_recus.money = f"{vente_paye_total} F"
        tableau_de_bord.payement_impayes.money = f"{vente_impaye_total} F"
        tableau_de_bord.total_des_depense.money = f"{depense_total} F"
        # except:
        #     pass
    #load user_data to screen
    def vente(self):
        screen_manager.transition.direction = "left"
        screen_manager.transition.duration= 0.1
        screen_manager.current= "add_vente"
    def depense(self):
        screen_manager.transition.direction = "left"
        screen_manager.transition.duration= 0.1
        screen_manager.current= "add_depense"
    def load_data(self, user_name, picture, email, number):
        screen_manager.get_screen("profile").user_name_1.secondary_text = user_name
        screen_manager.get_screen("profile").profile_image.source = picture
        screen_manager.get_screen("profile").email_1.secondary_text = email
        screen_manager.get_screen("profile").user_number.secondary_text = number
        screen_manager.get_screen("shop").profile_image.source = picture
        pass
    def build(self):
        #add icon to the app
        self.icon = "icon.png"
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("welcome.kv"))
        # screen_manager.add_widget(Builder.load_file("sign_up.kv"))
        # screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("gestion_vente.kv"))
        screen_manager.add_widget(Builder.load_file("add_depense.kv"))
        screen_manager.add_widget(Builder.load_file("add_vente.kv"))
        # screen_manager.add_widget(Builder.load_file("parametre_and_code.kv"))

        
        return screen_manager
    ############################
    # def login(self, id):
    #     if id==2:
    #         screen_manager.transition.direction = "left"
    #         screen_manager.current ="sign_up"
    #     elif id==3:
    #         screen_manager.transition.direction = "right"
    #         screen_manager.current ="login"
    #     elif id==4:
    #         screen_manager.transition.direction = "left"
    #         screen_manager.current ="login"
    # def data_login_on(self, nom_user, password):
    #     data={
    #             "nom": "Admin",
    #             "photo": "user_photo.png",
    #             "number": "+00012345678",
    #             "password": "Admin@Admin"
    #         }
    #     try:
    #         with open("user_data.json", "r", encoding="utf-8") as f:
    #             data = json.load(f)
    #     except:
    #         pass
    #     if nom_user == "":
    #         toast(f"imformation incorrectée...", duration=1)
    #     elif password != data["password"]:
    #         toast(f"imformation incorrectée...", duration=1)
    #     elif nom_user ==data["nom"] and password==  data["password"]:
    #         all=screen_manager.get_screen("gestion_des_vente_home").scr_acceeuil_org.profile_id.data.data1.data2
    #         all.user_name.text = data["nom"]
    #         all.user_number.text = data["number"]
    #         all.user_photo.source = data["photo"]
    #         screen_manager.get_screen("gestion_des_vente_home").scr_acceeuil_org.home_id.home_data.home_data1.home_data2.user_name_and_salut.text = f"Salut {data['nom']}"
    #         screen_manager.get_screen("gestion_des_vente_home").scr_acceeuil_org.home_id.home_data.home_data1.home_data2.user_photo.source = data["photo"]
    #         screen_manager.transition.direction = "left"
    #         screen_manager.current = "gestion_des_vente_home"
    #         toast(f"Connecté...", duration=1)
    #     else:
    #         toast(f"imformation incorrectée...", duration=3)
    # def sign_in(self, nom_user, user_photo, user_number, user_password, user_repassword_confirm):
    #     data={
    #                 "nom": nom_user,
    #                 "photo": user_photo,
    #                 "number": user_number,
    #                 "password": user_password
    #             }
    #     try:
    #         all=screen_manager.get_screen("gestion_des_vente_home").scr_acceeuil_org.profile_id.data.data1.data2
    #         all.user_name.text = data["nom"]
    #         all.user_number.text = data["number"]
    #         all.user_photo.source = data["photo"]
    #         screen_manager.get_screen("gestion_des_vente_home").scr_acceeuil_org.home_id.home_data.home_data1.home_data2.user_name_and_salut.text = f"Salut {data['nom']}"
    #         screen_manager.get_screen("gestion_des_vente_home").scr_acceeuil_org.home_id.home_data.home_data1.home_data2.picture.source = data["photo"]
    #         screen_manager.transition.direction = "left"
    #         screen_manager.current = "gestion_des_vente_home"
    #         toast(f"Connecté...", duration=1)
    #         with open("user_data.json", "w", encoding="utf-8") as f:
    #             json.dump(data, f, ensure_ascii=False, indent=4)
    #     except:
    #         pass
    # def add_picture(self):
    #     filechooser.open_file(on_selection= self.add_now)
    # def add_now(self, selected):
    #     if selected:
    #         image_profile= selected[0]
    #         screen_manager.get_screen("sign_up").picture.source =image_profile

####################################################
    # def add_stock(self, index):
    #     global dialog, stock, categorie, prix_in, prix_out, stock_init
    #     dialog = None
        
    #     if index==1:
            
    #         audio_name=MDTextField(hint_text="Name of the audio file", pos_hint={"center_y": .8, "center_x": .5}, size_hint_x=.7, text_color_normal="black", font_size="25sp")
    #         categorie=Spinner(text="French", values=([ i for i in ["Simple", "Moyen", "Bien", "Au top"]]), font_size="25sp",size_hint= (.45, .2), pos_hint={"center_x": .25, "center_y": .5})
    #         close_bt=MDRaisedButton(text="save", on_release=self.close_box, pos_hint={"center_x": .5, "center_y": .2},size_hint= (.5, .2), font_size="25sp")
    #         prix_in=MDTextField(hint_text="Prix d'achat", pos_hint={"center_y": .8, "center_x": .5}, size_hint_x=.7, text_color_normal="black", font_size="25sp")
    #         prix_out=MDTextField(hint_text="Prix de vente", pos_hint={"center_y": .8, "center_x": .5}, size_hint_x=.7, text_color_normal="black", font_size="25sp")
    #         stock_init=MDTextField(hint_text="Stock initial", pos_hint={"center_y": .8, "center_x": .5}, size_hint_x=.7, text_color_normal="black", font_size="25sp")
    #         float_layout=MDFloatLayout(
    #             audio_name,
    #             categorie,
    #             prix_out,
    #             stock_init,
    #             pos_hint={"center_x": .6, "center_y": .5})
    #         if not dialog:
    #             dialog=Popup(title= "Historique des Ventes",
    #                          title_color="black",
    #                             pos_hint={"center_x": .5, "center_y": .5},
    #                             size_hint= (.9, .6),
    #                             background="white"
    #                             )
    #             dialog.add_widget(float_layout)
    #         dialog.open()
    ############################################
    def add_vente_detail(self, date_achat, nom_client, numero_telephone, produit, montant, payement):
        # partie à bien analyser pour mieux les adaptées
        if montant== "":
            toast("Veuillez entrer le montant de la vente", duration=1)
            return
        if os.path.exists(fichier_for_products):
            with open(fichier_for_products, "r", encoding="utf-8") as file:
                produit_data= json.load(file)
        
        try:
            #add the product to the json file
            data={"date_achat":date_achat,
                "nom_client": nom_client,
                "numero_telephone": numero_telephone,
                "produit": produit,
                "montant": montant,
                "payement": payement
                }
            #vente dans la liste des historiques
            self.add_vente(date_achat, nom_client, numero_telephone, produit, montant, payement)
            #fonction pour ajouter les payant
            if payement=="Payé":
                produit_data["produits_paye"].append(data)
                with open(fichier_for_products, "w", encoding="utf-8") as file:
                    json.dump(produit_data, file, indent=4, ensure_ascii=False)
            #fonction pour ajouter les impayant
            else:
                produit_data["produits_impaye"].append(data)
                with open(fichier_for_products, "w", encoding="utf-8") as file:
                    json.dump(produit_data, file, indent=4, ensure_ascii=False)
            self.reload_tableau_de_bord()
        except Exception as e:
            print(f"An error occurred while adding the product: {e}")   
    def total_des_ventes_payes(self):
        if os.path.exists(fichier_for_products):
            with open(fichier_for_products, "r", encoding="utf-8") as file:
                produit_data= json.load(file)
        
            try:
                dat=([i for i in produit_data.get("produits_paye", [])])
                ventes_paye=sum(int(i["montant"]) for i in dat)
                return ventes_paye
            except FileNotFoundError:
                return 0
        else:
            return 0
    def add_vente(self, date_achat, nom_client, numero_telephone, produit, montant, payement):
        list_of_histo=screen_manager.get_screen("gestion_des_vente_home").navig.histo_des_ventes_id.histo_ventes_id.histo_list
        input_screen_data=screen_manager.get_screen("add_vente")
        input_screen_data.date_achat.text=""
        input_screen_data.nom_client.text=""
        input_screen_data.numero_telephone.text=""
        input_screen_data.produit.text=""
        input_screen_data.montant.text=""
        input_screen_data.payement.text=""
        list_of_histo.add_widget(Line_histo(date= date_achat,
                        client= nom_client,
                        numero_du_client= numero_telephone,
                        categorie= produit,
                        montant= montant,
                        paiement= payement))
        scroll_id_det=screen_manager.get_screen("gestion_des_vente_home").navig.histo_des_ventes_id.histo_ventes_id.scroll_id
        code_bottle =self.code_for_histo_bar()
        
        if code_bottle>=13:
            
            scroll_id_det.size_hint_y=0.99
            list_of_histo.size_hint_y=((2.2/24)*code_bottle)
    def total_des_ventes_impayes(self):
        
        if os.path.exists(fichier_for_products):
            with open(fichier_for_products, "r", encoding="utf-8") as file:
                produit_data= json.load(file)
            try:
                dat=([i for i in produit_data.get("produits_impaye", [])])
                ventes_impaye=sum(int(i["montant"]) for i in dat)
                return ventes_impaye
            except FileNotFoundError:
                return 0
        else:
            return 0
    
            
    def load_histo_des_ventes(self):
        # list_of_histo=screen_manager.get_screen("gestion_des_vente_home").navig.histo_des_ventes_id.histo_ventes_id.histo_list.clear_widgets()
        fichier_for_products="produits.json"
        def load_it(i):
            date_achat=i["date_achat"]
            nom_client=i["nom_client"]
            numero_telephone=i["numero_telephone"]
            produit=i["produit"]
            montant=i["montant"]
            payement=i["payement"]
            self.add_vente(date_achat, nom_client, numero_telephone, produit, montant, payement)
        if os.path.exists(fichier_for_products):
            with open(fichier_for_products, "r", encoding="utf-8") as file:
                produit_data= json.load(file)
            try:
                for i in produit_data["produits_impaye"]:
                    load_it(i)
            except:
                pass
            try:
                for i in produit_data["produits_paye"]:
                    load_it(i)
            except:
                pass
    def code_for_histo_bar(self):

        if not os.path.exists(fichier_for_products):
            return 0

        try:
            with open(fichier_for_products, "r", encoding="utf-8") as file:
                produit_data = json.load(file)

            produits_paye = produit_data.get("produits_paye", [])
            produits_impaye = produit_data.get("produits_impaye", [])

            code_bottle = len(produits_paye) + len(produits_impaye)

            
            return code_bottle

        except (json.JSONDecodeError, OSError, TypeError):
            return 0
    # ############################################
    def add_depense_detail(self, description, montant, data_inter, enter_categorie_categorie_enter):
        if montant== "":
            toast("Veuillez entrer le montant de la vente", duration=1)
            return
        if os.path.exists(fichier_for_products):
            with open(fichier_for_products, "r", encoding="utf-8") as file:
                produit_data= json.load(file)
        
        try:
            #add the expend to the json file
            data={"description":description,
                "montant": montant,
                "data_inter": data_inter,
                "enter_categorie_categorie_enter": enter_categorie_categorie_enter,
                }
            #depepnse dans la liste des historiques
            self.add_depense(description, montant, data_inter, enter_categorie_categorie_enter)
            #fonction pour ajouter les payant
            produit_data["depense"].append(data)
            with open(fichier_for_products, "w", encoding="utf-8") as file:
                json.dump(produit_data, file, indent=4, ensure_ascii=False)
            #fonction pour ajouter les impayant
            
        except Exception as e:
            print(f"An error occurred while adding the product: {e}")   
        self.reload_tableau_de_bord()

    def add_depense(self, description, montant, data_inter, enter_categorie_categorie_enter):
        
        list_of_histo=screen_manager.get_screen("gestion_des_vente_home").navig.histo_des_depenses_id.histo_depense_id.scroll_id.histo_list
        input_screen_data=screen_manager.get_screen("add_depense")
        input_screen_data.description.text=""
        input_screen_data.montant.text=""
        input_screen_data.data_inter.text=""
        input_screen_data.enter_categorie.text=""
        list_of_histo.add_widget(Depense_histo(date= data_inter,
                        description= description,
                        enter_categorie_categorie_enter= enter_categorie_categorie_enter,
                        montant= montant))
        scroll_id_det=screen_manager.get_screen("gestion_des_vente_home").navig.histo_des_depenses_id.histo_depense_id.scroll_id
        code_bottle =self.code_for_histo_bar_for_depense()
        
        if code_bottle>=13:
            
            scroll_id_det.size_hint_y=0.99
            list_of_histo.size_hint_y=((2.2/24)*code_bottle)

    def total_des_depenses(self):
        if os.path.exists(fichier_for_products):
            with open(fichier_for_products, "r", encoding="utf-8") as file:
                produit_data= json.load(file)
        
            try:
                dat=([i for i in produit_data.get("depense", [])])
                depenses=sum(int(i["montant"]) for i in dat)
                return depenses
            except FileNotFoundError:
                return 0
        else:
            return 0
    
    def load_histo_des_depenses(self):
        # list_of_histo=screen_manager.get_screen("gestion_des_vente_home").navig.histo_des_ventes_id.histo_ventes_id.histo_list.clear_widgets()
        fichier_for_products="produits.json"
        
        def load_it(i):
            description=i["description"]
            data_inter=i["data_inter"]
            montant=i["montant"]
            enter_categorie_categorie_enter=i["enter_categorie_categorie_enter"]
            self.add_depense(description, montant, data_inter, enter_categorie_categorie_enter)
        if os.path.exists(fichier_for_products):
            with open(fichier_for_products, "r", encoding="utf-8") as file:
                produit_data= json.load(file)

            try:
                
                for i in produit_data["depense"]:
                    load_it(i)
                    
            except:
                
                pass
    def code_for_histo_bar_for_depense(self):
        if not os.path.exists(fichier_for_products):
            return 0

        try:
            with open(fichier_for_products, "r", encoding="utf-8") as file:
                produit_data = json.load(file)

            depense = produit_data.get("depense", [])
            code_bottle = len(depense)
            return code_bottle

        except (json.JSONDecodeError, OSError, TypeError):
            return 0
    #####################################################################
    def contact_us(self, index):
        webbrowser.open(index)
if __name__=="__main__":
    MonCommerce().run()