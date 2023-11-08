import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_report(file_content, today_date):
    # Set up your email and SMTP server details
    sender_email = 'yunkang@regovtech.com'
    sender_password = 'Yunkang00--'
    # recipients = ['yuzanita.y@etiqa.com.my','shazalina.a@etiqa.com.my','nurlina.omar@etiqa.com.my','zuriyana_ab@etiqa.com.my','ainsuhara.n@etiqa.com.my']
    # cc_recipients = ['HANAsupport@regovtech.com', 'paul.agada@regovtech.com', 'ryanewe@regovtech.com']
    recipients = ['irfan.k@regovtech.com']
    cc_recipients = ['aina.tas@regovtech.com']
    smtp_server = 'smtp.gmail.com'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Use 587 for TLS or 465 for SSL

    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ', '.join(recipients)
    message['Cc'] = ', '.join(cc_recipients)
    message['Subject'] = f'HANA SUMMARY REPORT FOR {today_date}'

    # Create the HTML part of the message
    html_content = f'''
    <html>
      <body>
        <table width="650" cellspacing="0" cellpadding="0" border="0" style="color:rgb(136,136,136);font-family:&quot;Times New Roman&quot;">
        <tbody>
        <tr>
        <td>
        <table cellspacing="0" cellpadding="0" border="0"><tbody><tr><td valign="top" width="150" style="padding:10px 0px 0px;vertical-align:middle">
        <img width="200" height="66" src="https://ci3.googleusercontent.com/mail-sig/AIorK4zlM0MNSHRLcKMS8xKJOg2F-tIO9e1ZsDb7zsUjTEeF_Q5w1MKfbrT4mMB0wd8PO-oz800TmEk" class="CToWUd" data-bit="iit">
        </td>
        <td valign="top" style="font-size:1em;padding:0px 15px 0px 20px;vertical-align:top">
        <table cellspacing="0" cellpadding="0" border="0" style="line-height:1.4;font-family:Verdana,Geneva,sans-serif;font-size:14.4px;color:rgb(0,0,1)">
        <tbody>
        <tr>
        <td>
        <div style="font-weight:bold;font-stretch:normal;font-size:1.4em;line-height:normal">Lee Yun Kang
        </div>
        </td>
        </tr>
        <tr>
        <td style="padding:2px 0px"><div style="color:rgb(40,54,135);font-stretch:normal;font-size:1.05em;line-height:normal"><b>SRE &amp; AI Intern
        </b>
        </div>
        </td>
        </tr>
        <tr>
        <td style="padding:10px 0px 0px">
        <div style="color:rgb(40,54,135);font-weight:bold">ReGov Technologies Sdn Bhd (1246645-K)
        </div>
        </td>
        </tr>
        <tr>
        <td><span style="color:rgb(40,54,135);font-weight:bold">Tel:&nbsp;</span>
        <font face="Verdana, Geneva, sans-serif">+603 7650 4408 |&nbsp;</font>&nbsp;<span style="color:rgb(40,54,135);font-weight:bold">Mobile:&nbsp;</span><font face="Verdana, Geneva, sans-serif">+60 1624 86533</font><b style="color:rgb(53,28,117)"><br></b></td></tr><tr></tr><tr><td><span style="color:rgb(40,54,135);font-weight:bold">Email: yunkang</span><span style="color:rgb(40,54,135)"><a href="mailto:morris@regovtech.com" style="color:rgb(17,85,204)" target="_blank">@regovtech.com</a></span><span style="color:rgb(40,54,135);font-weight:bold"><br>Site:&nbsp;</span><a href="http://www.regovtech.com/" style="color:rgb(17,85,204)" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://www.regovtech.com/&amp;source=gmail&amp;ust=1699320502237000&amp;usg=AOvVaw3Oj6CfcWdw87WugutSzBvm">www.regovtech.com
        </a>
        </td>
        </tr>
        <tr>
        <td>
        <span style="color:rgb(40,54,135);font-weight:bold">Address:&nbsp;</span>C-7-01, Capital 3 │ Oasis Square │ No.2, Jalan PJU1A/7A │Ara Damansara │ 47301 Petaling Jaya, Selangor
        </td>
        </tr>
        </tbody>
        </table>
        </td>
        <td valign="middle" style="font-family:Arial;border-left:3px solid rgb(136,197,64);vertical-align:middle;padding:0px 0px 3px 6px;border-top-color:rgb(136,197,64);border-right-color:rgb(136,197,64);border-bottom-color:rgb(136,197,64)">
        <table cellspacing="0" cellpadding="0" border="0" style="line-height:1">
        <tbody>
        <tr>
        <td style="padding:4px 0px 0px"><img alt="" width="32" src="https://ci6.googleusercontent.com/proxy/UWdpgLgYSA6tJRQSh0evk9q1EK5YDNGWaIvIZSn5SE39nohrT2PTeAqrEDUVciqbXT9Y1CSZxfyLnuHd917KuC8-cL0DV_IV6vSHZhfeJnBVsm0=s0-d-e1-ft#https://drive.google.com/uc?id=16MkvMM-3g9zuuIUifQCKJ_qZC-PEqfwV" style="width:32px" class="CToWUd" data-bit="iit">
        </td>
        </tr>
        <tr>
        <td style="padding:4px 0px 0px">
        <img alt="" width="32" src="https://ci4.googleusercontent.com/proxy/ibydBeLH003oBFljl8stTrQ9_nVEE6CjnUhQasrFxefDrXmiWNz-4PLeZ8hWrEM6KgWJ8zZ6nWCQ6F0d3nfIHAjs0-EIud_jR_utpu4bFedwhjo=s0-d-e1-ft#https://drive.google.com/uc?id=1VdNvFOJ8bifbRITY2KWXHhUBybACC9yG" style="width:32px" class="CToWUd" data-bit="iit">
        </td>
        </tr>
        <tr>
        <td style="padding:4px 0px 0px">
        <img alt="" width="32" src="https://ci4.googleusercontent.com/proxy/FSn_KOQkjS6dclOIAOYszsoa0lRwD1hssK2neGqk_uhsbeFS6Ol54Wyy6llpKJcSSlUSMCG1z1HG2HknMlH-6JlG7xlk9gZJ2G_3KFRqS-kmvnM=s0-d-e1-ft#https://drive.google.com/uc?id=14AKK5EBAHeO--ANw6B8AJDjFOp9hBKmG" style="width:32px" class="CToWUd" data-bit="iit"><font color="#888888">
        <br>
        <br>
        </font>
        </td>
        </tr>
        </tbody>
        </table>
        </td>
        </tr>
        </tbody>
        </table>
        </td>
        </tr>
        </tbody>
        </table>
      </body>
    </html>
    '''

    body = """Hello Everyone,

    I hope this email finds you well. Please find attached the HANA Summary Report for """+today_date+""".

    Best Regards,



    """

    message.attach(MIMEText(body, 'plain'))



    file_part = MIMEApplication(file_content, _subtype="zip")
    file_part.add_header('Content-Disposition', 'attachment', filename=f'Hana Call Summary Full Report {today_date}.zip')
    message.attach(file_part)
    html_part = MIMEText(html_content, 'html')
    message.attach(html_part)


    try:
      # Create an SMTP object
      server = smtplib.SMTP(smtp_server, smtp_port)

      # Start TLS for security
      server.starttls()

      # Login to your email account
      server.login(sender_email, sender_password)

      # Send the email to recipients
      server.sendmail(sender_email, recipients, message.as_string())

      # Close the SMTP server
      server.quit()

      print("Email sent successfully!")

    except Exception as e:
      print(f"Email could not be sent. Error: {str(e)}")