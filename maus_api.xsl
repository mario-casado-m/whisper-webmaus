<?xml version="1.0" encoding="UTF-8"?>
<!-- Un archivo para transformar la documentacion de la API de WebMAUS -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    <xsl:template match="/CMD/Components/BASWebService/Service">
        <html>
            <head>
                <title>Docs WebMAUS</title>
                <style>
                    table, td {
                        border: 1px black solid;
                        padding: 5px;
                        border-collapse: collapse;
                       }
                    .parameter-name {
                        font-weight: bold;
                       }
                </style>
            </head>
            <body>
                <h1><xsl:value-of select="Name"/></h1>
                <p><xsl:value-of select="Description"/></p>
                <xsl:for-each select="//Operation">
                    <div>
                        <h2><xsl:value-of select="Name"/></h2>
                        <p><xsl:value-of select="Description"/></p>
                        <ul>
                            <xsl:for-each select="Input/Parameter">
                                <li>
                                    <span class="parameter-name"><xsl:value-of select="Name"/>: </span>
                                    <span><xsl:value-of select="Description"/></span>
                                    <ul>
                                        <xsl:for-each select="*">
                                            <xsl:choose>
                                                <xsl:when test="not(name()='Name') and not(name()='Description')">
                                                    <li>
                                                        <span class="parameter-name"><xsl:value-of select="name()"/>: </span>
                                                        <span class="new-line"><xsl:value-of select="."/></span>
                                                    </li>
                                                </xsl:when>
                                            </xsl:choose>
                                        </xsl:for-each>
                                    </ul>
                                </li>
                            </xsl:for-each>
                        </ul>
                    </div>
                </xsl:for-each>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
