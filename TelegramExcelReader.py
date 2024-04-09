# ExcelBotTelegram
# Consultar datos de Excel desde Telegram.
#@Author: Diego Villalobos
#@date: 16/02/2024


from telegram import Update, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters
import pandas as pd

# Configuración
TOKEN = 'TU_TOKEN_TELEGRAM'
RUTA_EXCEL = r'RUTA_HOJA_EXCEL'
NOMBRE_HOJA = 'NOMBRE_HOJA_EXCEL'
COLUMNAS = ['ID', 'NOMBRE', 'APELLIDO', 'TRABAJO']  # Lista de columnas en tu hoja de Excel
TRABAJO_BUSCADO = 'INGENIERO'

# Carga el archivo Excel en un DataFrame
df = pd.read_excel(RUTA_EXCEL, sheet_name=NOMBRE_HOJA, header=0)  # header=0 si los nombres de las columnas están en la primera fila

#---------------------------------------
#------ FUNCIÓN BUSQUEDA POR ID --------
#---------------------------------------
SOLICITAR_ID = 0

async def iniciar_solicitud_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Por favor, envíame el ID:')
    return SOLICITAR_ID

async def recibir_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    id_recibido = update.message.text
    try:
        id_recibido = int(id_recibido)
        resultado = df[df['ID'] == id_recibido].reset_index(drop=True)
        if not resultado.empty:
            fila = resultado.iloc[0]
            mensaje = '\n'.join([f"{col}: {fila[col]}" for col in COLUMNAS])
            await update.message.reply_text(mensaje)
        else:
            await update.message.reply_text("ID no encontrado.")
    except ValueError:
        await update.message.reply_text("Por favor, ingresa un número válido para el ID.")
    return ConversationHandler.END

async def cancelar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Operación cancelada.', reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

#--------------------------------------------
#----FUNCIÓN BUSQUEDA FILTRANDO COLUMNA------
#--------------------------------------------

async def filtrar_por_trabajo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    resultado = df[df['TRABAJO'].str.contains(TRABAJO_BUSCADO, case=False, na=False)]
    if not resultado.empty:
        mensaje = ''
        for _, fila in resultado.iterrows():
            mensaje += f"ID: {fila['ID']}\nNombre: {fila['NOMBRE']}\nApellido: {fila['APELLIDO']}\nTrabajo: {fila['TRABAJO']}\n\n"
        await update.message.reply_text(mensaje)
    else:
        await update.message.reply_text(f"No se encontraron registros con el trabajo 'INGENIERO'.")

#------------------------------------------------
#------Configuración de ConversationHandler------
#------------------------------------------------
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('buscar', iniciar_solicitud_id)],
    states={
        SOLICITAR_ID: [MessageHandler(filters.TEXT & ~filters.COMMAND, recibir_id)]
    },
    fallbacks=[CommandHandler('cancelar', cancelar)]
)

def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler('filtrar', filtrar_por_trabajo))
    
    application.run_polling()

if __name__ == '__main__':
    main()
