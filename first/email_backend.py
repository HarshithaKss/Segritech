import ssl
from django.core.mail.backends.smtp import EmailBackend as DjangoSMTPBackend

class CustomSMTPBackend(DjangoSMTPBackend):
    """
    Custom SMTP backend that handles SSL certificate verification issues
    by creating a more permissive SSL context for development/testing
    """
    
    def open(self):
        """
        Override the open method to use a custom SSL context
        """
        if self.connection:
            return False
            
        # Create SSL context that's more permissive for development
        connection_params = {
            'host': self.host,
            'port': self.port,
            'username': self.username,
            'password': self.password,
            'use_tls': self.use_tls,
            'use_ssl': self.use_ssl,
            'timeout': self.timeout,
        }
        
        try:
            # Create custom SSL context
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            
            # Import smtplib here to avoid circular imports
            import smtplib
            
            self.connection = smtplib.SMTP(self.host, self.port, timeout=self.timeout)
            
            if self.use_tls:
                self.connection.starttls(context=ssl_context)
            elif self.use_ssl:
                # For SSL, we need to create the connection differently
                self.connection = smtplib.SMTP_SSL(self.host, self.port, 
                                                  timeout=self.timeout, 
                                                  context=ssl_context)
            
            if self.username and self.password:
                self.connection.login(self.username, self.password)
                
            return True
        except Exception as e:
            print(f"Failed to connect to SMTP server: {e}")
            if not self.fail_silently:
                raise
            return False 