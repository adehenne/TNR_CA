import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testng.keyword.TestNGBuiltinKeywords as TestNGKW
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

WebUI.openBrowser('')

WebUI.maximizeWindow()

WebUI.navigateToUrl(GlobalVariable.URL)

WebUI.click(findTestObject('Page_Accueil/bouton_acces_auth'))

WebUI.setText(findTestObject('Page_Authentification/champs_username'), user)

WebUI.setMaskedText(findTestObject('Page_Authentification/champs_password'), pw)

WebUI.click(findTestObject('Page_Authentification/bouton_connexion'))

WebUI.click(findTestObject('Page_Bienvenue/bouton_Menu_Credit'))

WebUI.click(findTestObject('Page_Bienvenue/bouton_creer_contrat'))

WebUI.setText(findTestObject('Object Repository/Page_Simulation_Credit/champs_montant_achat'), '20000')

WebUI.setText(findTestObject('Object Repository/Page_Simulation_Credit/champs_montant_credit'), '')

WebUI.click(findTestObject('Object Repository/Page_Simulation_Credit/champs_montant_credit'))

WebUI.setText(findTestObject('Object Repository/Page_Simulation_Credit/champs_montant_credit'), '17000')

WebUI.setText(findTestObject('Object Repository/Page_Simulation_Credit/champs_duree'), '20')

WebUI.click(findTestObject('Object Repository/Page_Simulation_Credit/bouton_calculer_credit'))

WebUI.click(findTestObject('Object Repository/Page_Simulation_Credit/bouton_echeancier'))

WebUI.click(findTestObject('Object Repository/Page_Simulation_Credit/bouton_creer_contrat'))

WebUI.setText(findTestObject('Page_Recherche_Client/champs_nom'), nomClient)

WebUI.setText(findTestObject('Page_Recherche_Client/champs_prenom'), prenomClient)

WebUI.click(findTestObject('Page_Recherche_Client/bouton_rechercher'))

WebUI.executeJavaScript('document.querySelector("#customControlValidation2").click()', [])

WebUI.click(findTestObject('Page_Recherche_Client/bouton_valider'))

WebUI.click(findTestObject('Page_Impr_Enr_Contrat/bouton_imprimer'))

WebUI.switchToWindowIndex(0)

WebUI.click(findTestObject('Page_Impr_Enr_Contrat/bouton_enregistrer'))

WebUI.verifyElementPresent(findTestObject('Page_Impr_Enr_Contrat/message_succes_enr_contrat'), 0)

WebUI.click(findTestObject('Menu/bouton_deconnexion'))

WebUI.closeBrowser()

