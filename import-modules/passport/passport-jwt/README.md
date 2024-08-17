# Passport-jwt Documentaion

## Table of Contents

1. [Overview](#features-and-usage) 
2. [Features and Usage](#features-and-usage)
3. [Authentication](#authenticating-jwt-after-strategy-configuration)
4. [Passing Jwt Token](#sending-jwt-from-client-to-server)

## Overview

- A middleware for Express.js framework that provides authentication and authorization using JSON Web Tokens (JWT).
- A passport strategy to work with JWT
- This only handles what we can do with a JWT token created using passport. To create a token checkout [Passport](http://passportdocumentation)

## Features and Usage

1.  Installation and Import
    - Install: `npm install passport-jwt`
    - Import: `const { Strategy, ExtractJwt } = require("passport-jwt");`
      - _passport-jwt is a class with 2 properties - Strategy and ExtractJwt_
      - _Strategy is a class with 2 parameters passed to its contructor_
      - _ExtractJwt is an object with various sub properties_
2.  Configuration

    - Basic Structure:

      ```javascript
      const JwtStrategy = require("passport-jwt").Strategy;
      const ExtractJwt = require("passport-jwt").ExtractJwt;
      const passport = require("passport");

      // Options for the strategy
      const opts = {
        jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(), // Extract token from Authorization header
        secretOrKey: "your_jwt_secret_key", // Secret key for verifying token
      };

      // JWT Strategy
      passport.use(
        new JwtStrategy(opts, (jwtPayload, done) => {
          // Find the user based on the jwtPayload.sub (subject)
          User.findOne({ id: jwtPayload.sub }, (err, user) => {
            if (err) {
              return done(err, false);
            }
            if (user) {
              return done(null, user);
            } else {
              return done(null, false); // User not found
            }
          });
        })
      );
      ```

    - Parts of the configuration:

      1. Imports:
         - `const {Strategy,ExtractJwt} = require("passport-jwt")`
         - `const passport = require("passport");`
      2. passport.use() method to register strategy (2 ways):
         <details>
             <summary>
             <code>passport.use(Strategy)</code> - Default Strategy
             </summary>

         - Registers a strategy directly.
         - Will be treated as the default strategy.
         - Allows you to refer to the strategy by the name _jwt_ later in the *passport* method `passport.authenticate('jwt')`.
         </details>

         <details>
             <summary>
             <code>passport.use(name, Strategy)</code> - Named Strategy [optional]
             </summary>

         - Allows you to refer to the strategy by the name _jwt_ later in the *passport* method `passport.authenticate('name')`.
         </details>
      3. Strategy (has 2 parameters):
            - Has two parameters: `opts` and `verify`
            
            - Parameters:
                <details>
                <summary>
                    <code>`opts`</code> - (object) Options
                </summary>
                
                - This parameter is an object that defines various options for the strategy.

                - Example:
                    ```js
                    const opts = {
                        jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
                        secretOrKey: "your_jwt_secret_key",
                        issuer: "your_issuer", // optional
                        algorithms: ["HS256"], // optional
                        ignoreExpiration: false, // optional, defaults to false
                    };
                    ```
                - Properties:

                    - <details>
                            <summary>
                            <code>jwtFromRequest</code> - (function) To specify method of Jwt extraction
                            </summary>

                        - Specifies how the JWT will be extracted from the incoming request from client using _ExtractJwt_ class.
                        - Example
                            ```javascript
                            const opts = {
                                jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken();
                            }
                            ```

                        - All options (Properties of ExtractJwt):

                        - <details>
                            <summary>
                            <code>ExtractJwt.fromAuthHeaderAsBearerToken()</code>
                            </summary>

                            - **Usage**: Extracts the JWT from the Authorization header, assuming the JWT is prefixed by the word Bearer.
                            - **Input parameter**: none
                            - **Example**:

                            ```js
                            jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken();
                            ```

                            </details>

                        - <details>
                            <summary>
                            <code>ExtractJwt.fromHeader(headerName)</code>
                            </summary>

                            - **Usage**: Extracts the JWT from a custom header in the request.
                            - **Input parameter**: headerName (string) - The name of the custom header containing the JWT.
                            - **Example**:

                            ```js
                            jwtFromRequest: ExtractJwt.fromHeader('auth_token')
                            ```

                            </details>


                        - <details>
                            <summary>
                            <code>ExtractJwt.fromBodyField(fieldName)</code>
                            </summary>

                            - **Usage**:  Extracts the JWT from a specific field in the request body (typically used in form submissions or JSON payloads).
                            - **Input parameter**: fieldName (string) - The name of the field in the request body that contains the JWT.
                            - **Example**:

                            ```js
                            jwtFromRequest: ExtractJwt.fromBodyField('token')
                            ```

                            </details>

                        - <details>
                            <summary>
                            <code>ExtractJwt.fromUrlQueryParameter(parameterName)</code>
                            </summary>

                            - **Usage**:  Extracts the JWT from a URL query parameter.
                            - **Input parameter**: parameterName (string) - The name of the query parameter in the URL that contains the JWT.
                            - **Example**:

                            ```js
                            jwtFromRequest: ExtractJwt.fromUrlQueryParameter('token')
                            ```
                            </details>
                        
                        - <details>
                            <summary>
                            <code>fromAuthHeaderWithScheme(auth_scheme) </code>
                            </summary>

                            - **Usage**:  Extracts the JWT from Authorization Header with the specified auth_scheme
                            - **Input parameter**: (string) Auth scheme like Bearer, Token, etc
                            - **Example**:

                                ```js
                                jwtFromRequest: ExtractJwt.ExtractJwt.fromAuthHeaderWithScheme('Token')
                                ```
                            </details>

                        - <details>
                            <summary>
                            <code>fromExtractors([array of extractor functions]) </code>
                            </summary>

                            - **Usage**:  Lets us define multiple extractors to extract jwt from different sources one after other.
                            - **Input parameter**: (array) Array of extractors
                            - **Example**:

                                ```js
                                const extractors = [
                                    ExtractJwt.fromAuthHeaderAsBearerToken(),         // Try the Bearer token from Authorization header
                                    ExtractJwt.fromUrlQueryParameter('auth_token')    // Then try the token from the URL query parameter
                                ];

                                const opts = {
                                    jwtFromRequest: ExtractJwt.fromExtractors(extractors),
                                    secretOrKey: 'your_secret_key'
                                };
                                ```
                            </details>
                        
                        - <details>
                            <summary>
                            <code>Custom Extractors</code>
                            </summary>

                            - **Usage**:  Lets us define custom extractoinof tokens from anywhere
                            - **Example**:
                                ```js
                                //when extracting from cookies using cookie parser
                                var cookieParser = require('cookie-parser')
                                const express = require('express');

                                const app = express()
                                app.use(cookieParser())
                                
                                //custom extractor
                                var cookieExtractor = function (req) {
                                var token = null;
                                if (req && req.cookies) {
                                    token = req.cookies["jwt"];
                                }
                                return token;
                                };

                                const opts = {
                                    jwtFromRequest: cookieExtractor,
                                    secretOrKey: 'your_secret_key'
                                };
                                ```
                            </details>


                        </details>

                    - <details>
                        <summary>
                            <code>secretOrKey</code> - (string or buffer) Secret key to verify JWT
                        </summary>

                        - The key used to verify the JWT signature. This is essential for validating the authenticity of the token.

                        - **For symmetric algorithms** (e.g., HS256, HS384, HS512), `secretOrKey` will be a shared secret string or buffer used by both the server that signs the JWT and the server that verifies it.
                        - **For asymmetric algorithms** (e.g., RS256, RS384, RS512), `secretOrKey` will be a public key that verifies the JWT, while the corresponding private key is used to sign the JWT.

                        - Examples:
                            - Symmetric key:
                                ```js
                                const opts = {
                                    secretOrKey: 'your_jwt_secret_key' //can be any random word
                                };
                                ```
                            - Asymmetric key:
                                ```js
                                const opts = {
                                    secretOrKey: fs.readFileSync('./path/to/public.key', 'utf8')
                                };
                                ```
                            > [!NOTE] <br>
                            > If using symmetric encryption (e.g., HS256), the same secretOrKey must be used for both signing and verifying the token. <br>
                            > If using asymmetric encryption (e.g., RS256), the secretOrKey should be the public key, while the private key is used to sign the token. <br>
                            > It is important to securely manage this key, as exposure could compromise the security of your system.
                        </details>

                    - <details>
                        <summary>
                            <code>secretOrKeyProvider</code> - (function) [optional] Function to get secretOrKey from anywhere
                        </summary>

                        - This function dynamically provides the secret or public key for verifying the JWT. It is useful in cases where the key needs to be determined based on the request, such as in multi-tenant applications or when using different keys for different users.
                        - Do not use both `secretOrKey` and `secretOrKeyProvider`. Use either of them
                        - Parameters:
                            - `request`: The original HTTP request object.
                            - `rawJwtToken`: The raw JWT token extractedfrom the request.
                            - `done`: Callback function to return the key. The first parameter of done is an error (if any), and the second is the secret or public key.
                        - Example:
                            ```js
                                const opts = {
                                    secretOrKeyProvider: (request, rawJwtToken, done) => {
                                        // Logic to determine the secret or key dynamically
                                        const secretOrKey = getSecretForTenant(request); // Example function to get the secret key based on tenant
                                        done(null, secretOrKey); // Pass the key to the callback function
                                    }
                                };
                            ```

                            > [!NOTE] <br>
                            > 1. If secretOrKeyProvider is provided, it overrides the static secretOrKey option.<br>
                            > 2. Useful in scenarios where the key might change per request or per user, such as:
                            >    - Multi-tenant applications where each tenant has a different key.
                            >    - Using different keys for different users or services.
                            > 3. If the key cannot be determined (e.g., a database lookup fails), call done(err) to signal an error.
                            > 4. When using asymmetric encryption (e.g., RS256), the secretOrKeyProvider would return the public key for verification.

                            - Example for multi-tenant application:
                                ```js
                                const opts = {
                                    secretOrKeyProvider: (request, rawJwtToken, done) => {
                                        // Get the tenant's key based on some property of the request (e.g., subdomain or user ID)
                                        const tenantKey = getTenantKeyFromDb(request.tenantId); // Example function to retrieve tenant's key
                                        done(null, tenantKey);
                                    }
                                };
                                ```
                            - Use Case:
                                - Multi-tenant systems where different tenants have different signing keys.
                                - Dynamic environments where the key cannot be determined statically and must be retrieved or computed based on the incoming request.
                        </details>

                    - <details>
                            <summary>
                            <code>issuer</code> - (string or array) [optional]  Verifies the issuer (iss) claim of the token.
                            </summary>
                            - Examples:
                            
                            ```js
                            const opts = {
                                        issuer: 'https://accounts.google.com'
                                    };
                            ```
                            ```js
                            const opts = {
                                    issuer: [
                                        'https://accounts.google.com',
                                        'https://your-tenant-name.auth0.com/',
                                        'https://dev-123456.okta.com'
                                    ]
                                };
                            ```
                            - Use Cases:
                                - **Single Issuer Application**: If all tokens are issued by your application, you would set the issuer option to your app's identifier.
                                - **Third-Party Tokens**: If you're working with tokens issued by third parties (e.g., OAuth providers or external identity systems), you would set issuer to the known trusted issuer.
                        </details>

                    - <details>
                        <summary>
                        <code>algorithms</code> - (array) [optional] List of allowed algorithms for token verification, e.g., ['HS256', 'RS256'].
                        </summary>

                        - **Purpose**: This option helps enforce which algorithms are accepted for signing JWTs, improving security by rejecting tokens signed with algorithms that are not trusted or expected.
                        - **Default Behavior**: If the algorithms option is not provided, the strategy will allow any algorithm,
                        - Examples:
                            ```js
                            const opts = {,
                                algorithms: ['HS256', 'RS256', 'ES256'] // Accepts JWTs signed with HS256, RS256, or ES256 algorithms
                            };
                            ```
                            ```js
                            const opts = {,
                                algorithms: ['HS256']
                            };
                            ```
                        </details>

                    - <details>
                        <summary>
                        <code>audience</code> - (string or array) [optional] To specify the recipients of Jwt
                        </summary>

                        - **Purpose**: To specify the recipients of Jwt. Will be verifiesd against the recipients mentioned in *aud* coming through *jwt_payload*.
                        - Examples:
                            ```js
                            const opts = {,
                                 "aud": "user-service",
                            };
                            ```
                            ```js
                            const opts = {,
                                 "aud": ["user-service", "billing-service", "yoursite.net"]
                            };
                            ```
                        </details>

                    - <details>
                            <summary>
                            <code>ignoreExpiration</code> - (boolean) [optional] Whether to ignore the token's expiration time during verification.
                            </summary>

                            - **Purpose**: 
                                - When you want to accept tokens even if they have expired.
                                - Useful in testing environments where you might not want to deal with token expiration.
                                - The `exp` claim in a JWT specifies the expiration time of the token. Expiry is not set by passport-jwt.
                            - **Default Behavior**: By default, ignoreExpiration is false, meaning that Passport-JWT will check the exp claim to ensure the token is not expired.
                            - Examples:
                                ```js
                                const opts = {
                                    ignoreExpiration: true // Accepts expired tokens
                                };
                                ```
                                ```js
                                const opts = {
                                    ignoreExpiration: false // Enforces expiration check
                                };
                                ```
                        </details>

                    - <details>
                        <summary>
                        <code>passReqToCallback</code> - (boolean) [optional] Whether to pass the request object to the verification callback.
                        </summary>

                        - The `passReqToCallback` option specifies whether the request object should be passed to the `verify` callback function in the `JwtStrategy`. 
                        - Useful if you need access to the `req` object for additional logic inside verify callback.
                        - Example:
                            ```js
                            const opts = {
                                passReqToCallback: true // Passes the request object to the verify callback
                            };
                            ```
                            ```js
                            passport.use(new JwtStrategy(opts, (req, jwtPayload, done) => { //now you can add req as parameter
                                // Access request object
                                console.log(req.headers); // Example of accessing headers

                                User.findById(jwtPayload.sub, (err, user) => {
                                    if (err) return done(err, false);
                                    if (user) return done(null, user);
                                    return done(null, false);
                                });
                            }));
                            ```
                        </details>
                    
                    - <details>
                        <summary>
                        <code>jsonWebTokenOptions </code> - (object) [optional] To pass options to customise token verification
                        </summary>

                        - **Purpose**: To pass options directly to the underlying jsonwebtoken.verify() and customise token verification.
                        - **Properties**: 
                            - `clockTolerance`: (integer) Helps with clock skew issues.
                            - `maxAge`: (string) Limits how old a token can be.
                            - `algorithms`: (array) Specifies allowed signing algorithms.
                            - `ignoreNotBefore`: (boolean) Ignores the nbf claim if true.
                            - `ignoreExpiration`: (boolean) Ignores the exp claim if true.
                        - Examples:
                            ```js
                            const opts = {
                                jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
                                secretOrKey: 'your_secret_key',
                                jsonWebTokenOptions: {
                                    clockTolerance: 5,  // Allow 5 seconds of clock skew
                                    maxAge: '1d',       // Only accept tokens no more than 1 day old
                                    algorithms: ['HS256'],  // Only accept tokens signed with HS256
                                    ignoreNotBefore: true, // Will ignore token's Not before dates
                                    ignoreExpiration: false // Will validate the 'expiration' claim
                                }
                            };

                            passport.use(new JwtStrategy(opts, (jwtPayload, done) => {
                                User.findById(jwtPayload.sub, (err, user) => {
                                    if (err) return done(err, false);
                                    if (user) return done(null, user);
                                    return done(null, false);
                                });
                            }));
                            ```
                        </details>

                </details>
            
                <details>
                <summary>
                    <code>`verify`</code> - (function) Verify Callback
                </summary>

                - **Purpose**: Callback used in the `JwtStrategy` to validate the JWT and determine if it should be accepted.
                - **Parameters**: 
                    - <details>
                        <summary>
                        <code>jwtPayload</code> - (object) Payload for verify callback
                        </summary>

                        - **Purpose**: It is the decoded JWT payload, which contains the claims from the token (e.g., user ID, roles). 
                        - It is an object that contains the claims from the decoded JWT. We can only access these claim values and set it. It is set using *jwt.sign()* using [*jsonwebtoken*](http://jwtdocumentation) module.
                        - **Properties**  **(Claims)**:
                            1. `sub`: The **subject** of the token, usually the user ID. This is a standard claim and is often used to identify the user.
                            2. `exp`: The **expiration** time of the token, specified as a Unix timestamp. This is a standard claim used to determine if the token has expired.
                            3. `iat`: The **issued-at** time, specified as a Unix timestamp. This indicates when the token was issued.
                            4. `iss`: The **issuer** of the token, which is a standard claim indicating who issued the token.
                            5. `aud`: The **audience** for which the token is intended. This is a standard claim indicating the recipient(s) of the token. 
                            6. `nbf`: **Not Before** - The time before which the token should not be considered valid.
                            7. `jti`: **JWT ID** - A unique identifier for the token, which can be used to prevent replay attacks.
                            > [!NOTE] <br>
                            > we can also have any custom claims. eg: roles, name.
                        - Example:
                            ```js
                            //setting claims in some other file
                            const jwt = require('jsonwebtoken')
                            fucntion signIn(req, res){
                                const payload = {
                                    sub: user._id, 
                                    roles: user.roles, 
                                    exp: Math.floor(Date.now() / 1000) + (60 * 60) 
                                    //etc
                                }
                                const token = jwt.sign(payload, 'your_jwt_secret_key')
                                res.send({token})
                            }

                            //accessing those claims
                            passport.use(new JwtStrategy(opts, (jwtPayload, done) => {
                                console.log('User ID:', jwtPayload.sub); 
                                console.log('Token Expiry Time:', jwtPayload.exp); 
                                console.log('User Roles:', jwtPayload.roles);

                                User.findById(jwtPayload.sub, (err, user) => {
                                    if (err) return done(err, false);
                                    if (user) return done(null, user);
                                    return done(null, false);
                                });
                            }));

                            ```
                        </details>

                    - <details>
                        <summary>
                        <code>done</code> - (fucntion) To indicate the result of the verification.
                        </summary>

                        - **Purpose**: To indicate the result of the verification.
                        - **Parameters**:
                            - `err`: Error during verification if any
                            - `user`: Any sort of data that comes out after the logic inside verify callback
                            - `info`: [optional] Any message regarding error or user
                        - Example:
                            ```js
                            //without info
                            passport.use(new JwtStrategy(opts, (jwtPayload, done) => {
                                User.findById(jwtPayload.sub, (err, user) => {
                                    if (err) return done(err, false);
                                    if (user) return done(null, user); // Verification successful
                                    return done(null, false); // No user found, but no error
                                });
                            }));
                            ```
                            ```js
                            //with info
                            passport.use(new JwtStrategy(opts, (jwtPayload, done) => {
                                User.findById(jwtPayload.sub, (err, user) => {
                                    if (err) return done(err, false);
                                    if (!user) return done(null, false, { message: 'User not found' });
                                });
                            }));
                            ```
                          </details>
                - Example:
                    ```js
                    const verify = (jwtPayload, done) => {
                        // jwtPayload contains the decoded JWT payload
                        User.findById(jwtPayload.sub, (err, user) => {
                            if (err) return done(err, false); // Error during user lookup
                            if (user) return done(null, user); // User found, authentication successful
                            return done(null, false); // User not found, authentication failed
                        });
                    }

                    passport.use(new JwtStrategy(opts, verify));
                    ```
                 </details>

            - Example:
                ```js
                const JwtStrategy = new Startegy(opts, verify)
                passport.use(JwtStrategy);
                ```
        

    3.  Full Structure (for deafult strategy):
        - Default Strategy:
            ```javascript
            const { Strategy, ExtractJwt } = require("passport-jwt");
            const passport = require("passport"); //to use for passport.use()

            // Options for the strategy
            const opts = {
                jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
                secretOrKey: "your_jwt_secret_key",
                //etc
            };

            //verify callback for strategy
            const verify = (jwtPayload, done) => {
                User.findOne({ id: jwtPayload.sub }, (err, user) => {
                if (err) {
                    return done(err, false);
                }
                if (user) {
                    return done(null, user);
                } else {
                    return done(null, false); // User not found
                }
                });
            };

            //new jwt-Strategy
            const JwtStrategy = new Strategy(opts, verify)

            //using new jwt-strategy in passport
            passport.use(JwtStrategy);

            //authenticating default jwt-strategy
            passport.authenticate('jwt')
            ```

        - Named Strategy:
            ```javascript
            const { Strategy, ExtractJwt } = require("passport-jwt");
            const passport = require("passport"); 

            const opts = {
                jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
                secretOrKey: "your_jwt_secret_key",
                //etc
            };

            const verify = (jwtPayload, done) => {
                User.findOne({ id: jwtPayload.sub }, (err, user) => {
                if (err) {
                    return done(err, false);
                }
                if (user) {
                    return done(null, user);
                } else {
                    return done(null, false); 
                }
                });
            };

            const JwtStrategy = new Strategy(opts, verify)

            //using named jwt-strategy in passport
            passport.use('my-jwt', JwtStrategy);

            //authenticating named jwt-strategy
            passport.authenticate('my-jwt')
            ```



## Authenticating jwt after strategy configuration
- The call function to call the strategy configured above is `passport.authenticate()`
- `passport.authenticate()` is a passport middleware. It has been [customised internally](https://github.com/mikenicholson/passport-jwt/blob/master/lib/strategy.js#L90) to authenticate jwt via passport-jwt package.
- It is set as an express middleware in order to use req, res, and
- Parameters:
    - <details>
        <summary>
            <code>strategy</code>: (string or array)
        </summary>

        - **Purpose**: To point to the strategies named during configuration.
        - **Example**: jwt, my-jwt, [jwt, my-jwt], etc
    </details>

        
    - <details>
        <summary>
            <code>options</code>: (object) [optional]
        </summary>

        - **Purpose**: Options to control the behavior of the authentication middleware.
        - **Properties**:
            1. <details>
                <summary>
                    <code>session</code>: (Boolean)
                </summary>

                - **Description**: Whether to use sessions. Typically set to false for JWT strategies.
                - **Default**: true
                </details>

            2. <details>
                <summary>
                    <code>failureRedirect</code>: (String)
                </summary>

                - **Description**: URL to redirect to if authentication fails.
                - **Default**: undefined
                </details>

            3. <details>
                <summary>
                    <code>failureFlash</code>: (Boolean or String)
                </summary>

                - **Description**: Flash message to display if authentication fails.
                - **Default**: undefined
                </details>

            4. <details>
                <summary>
                    <code>successRedirect</code>: (String)
                </summary>

                - **Description**: URL to redirect to upon successful authentication.
                - **Default**: undefined
                </details>

            5. <details>
                <summary>
                    <code>successMessage</code>: (String)
                </summary>

                - **Description**: Message to send upon successful authentication.
                - **Default**: undefined
                </details>

            6. <details>
                <summary>
                    <code>failureMessage</code>: (String)
                </summary>

                - **Description**: Message to send upon failed authentication.
                - **Default**: undefined
                </details>

            7. <details>
                <summary>
                    <code>scope</code>: (Array)
                </summary>

                - **Description**: Specifies required scopes for OAuth-based strategies.
                - **Default**: undefined
                </details>

            8. <details>
                <summary>
                    <code>passReqToCallback</code>: (Boolean)
                </summary>

                - **Description**: Whether to pass the request object to the verify callback function.
                - **Default**: false
                </details>
    </details>


    - <details>
        <summary>
            <code>callback</code>: (function) [optional]
        </summary>

        - **Purpose**: Handles the result of the authentication process and provides feedback or further actions based on the outcome.

        - **Parameters**:
            1. <details>
                <summary>
                    <code>err</code>: (Error or <code>null</code>)
                </summary>

                - **Description**: Contains any error that occurred during the authentication process.
                - **Type**: `Error` or `null`
                - **Example**: An error object if something went wrong, otherwise `null`.
                </details>

            2. <details>
                <summary>
                    <code>user</code>: (User object or <code>false</code>)
                </summary>

                - **Description**: The authenticated user object if authentication was successful, or `false` if no user was authenticated.
                - **Type**: User object or `false`
                - **Example**: The user data retrieved from the database if authentication is successful.
                </details>

            3. <details>
                <summary>
                    <code>info</code>: (Object or <code>false</code>)
                </summary>

                - **Description**: Contains additional information or error messages about the authentication process. This can include details about why authentication failed.
                - **Type**: Object or `false`
                - **Example**: An object with a `message` property if authentication fails, or `false` if no additional information is available.
                </details>

            4. <details>
                <summary>
                    <code>status</code>: (HTTP Status Code)
                </summary>

                - **Description**: The HTTP status code representing the result of the authentication attempt.
                - **Type**: Number (HTTP status code)
                - **Example**: `401` for unauthorized access, `200` for successful authentication.
                </details>
    </details>




- Examples:
    ```js
    //default strategy without optional parameters
    app.post("/profile", (req, res, next) => {
        passport.authenticate("jwt")(req, res, next)
    });
    ```
     ```js
    //custom strategy without optional parameters
    app.post("/profile", (req, res, next) => {
        passport.authenticate("my-jwt")(req, res, next)
    });
    ```
    ```js
    //default strategy with optional parameters
    app.post("/profile", (req, res, next) => {
        passport.authenticate("jwt", { session: false }, function(err, user, info) {
            if (err) {
                return res
                        .status(500)
                        .json({ message: 'An error occurred', error: err });
            }

            if (!user) {
                return res
                        .status(401)
                        .json({ message: 'Unauthorized', info: info });
            }

            //in case of callback we need to set req.user=user
            req.user=user

            res.json(user.profile);
        })(req, res, next)
    });
    ```

## Sending jwt from client to server
1. <details>
    <summary>
    Using Authorisation header (most common)
    </summary>

    - <details>
        <summary>
        Bearer Token: The most common and standard method for JWTs.
        </summary>

        ```js
        // Client-side (e.g., using Axios in JavaScript)
        axios.get('/protected-resource', {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        // Server-side (Express with Passport)
        const opts = {
            jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(), // Extract JWT from Bearer Token
            secretOrKey: SECRET_KEY,
        }
        ```
        <details>

    - <details>
        <summary>
        Custom Scheme: Allows custom authentication schemes as needed.
        </summary>

        ```js
        // Client-side (e.g., using Axios in JavaScript)
        axios.get('/protected-resource', {
             headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        // Server-side (Express)
        const customSchemeExtractor = (req) => {
            const authHeader = req.headers['authorization'];
            if (authHeader && authHeader.startsWith('customScheme ')) {
                return authHeader.split(' ')[1];
            }
            return null;
        };
       
       const opts = {
            jwtFromRequest: customSchemeExtractor, // Use custom extractor
            secretOrKey: SECRET_KEY,
        }
        ```
        <details>

    - <details>
        <summary>
        Digest Authentication: Less common for JWTs, used in specific scenarios.
        </summary>

        ```js
        // Client-side (e.g., using Axios in JavaScript)
        axios.get('/protected-resource', {
             headers: {
                'Authorization': `Digest ${token}`
            }
        });

        // Server-side (Express)
        const digestExtractor = (req) => {
            const authHeader = req.headers['authorization'];
            if (authHeader && authHeader.startsWith('Digest ')) {
                return authHeader.split(' ')[1];
            }
            return null;
        };
       
       const opts = {
            jwtFromRequest: digestExtractor, // Use custom extractor
            secretOrKey: SECRET_KEY,
        }
        ```
        <details>

    - <details>
        <summary>
        Basic Authentication: Typically used for credentials, not recommended for JWTs.
        </summary>

        ```js
        // (Not Recommended for JWTs)
        // Client-side (e.g., using Axios in JavaScript)
        axios.get('/protected-resource', {
             headers: {
                'Authorization': `Basic ${token}`
            }
        });

        // Server-side (Express)
        const basicExtractor = (req) => {
            const authHeader = req.headers['authorization'];
            if (authHeader && authHeader.startsWith('Basic ')) {
                return authHeader.split(' ')[1];
            }
            return null;
        };
       
       const opts = {
            jwtFromRequest: basicExtractor, // Use custom extractor
            secretOrKey: SECRET_KEY,
        }
        ```
        <details>
    </details>

2. <details>
    <summary>
    Using cookies
    </summary>

    - For client side:
        - We dont have to do anything. just run both server an dclient on same url (eg: http://localhost:3000), client using build file and server direclty running using node index.
        - when both run on same server:
            - cookies sent to client from sever will be stored as Set-Cookies in header and 
            - server itself will read it back when any req is sent from client to server
        ```js
        //client side 
        axios.get('/protected-resource')

        // server side
        const cookieParser = require('cookie-parser')
        const express = require('express');

        const app = express()
        app.use(cookieParser())

        //custom extractor
        var cookieExtractor = function (req) {
        var token = null;
        if (req && req.cookies) {
            token = req.cookies["jwt"];
        }
        return token;
        };

        const opts = {
            jwtFromRequest: cookieExtractor,
            secretOrKey: 'your_secret_key'
        };
        ```
    </details>

3. <details>
    <summary>
    Using URL Query Parameters
    </summary>

    ```js
    // Client-side (e.g., using Axios)
    axios.get('/protected-resource?token=' + token)   

    // Custom extractor function for query parameters
    const queryParamExtractor = (req) => {
        return req.query.token; // Extract JWT from query parameter 'token'
    };   

    const opts = { 
        jwtFromRequest: queryParamExtractor, // Use custom extractor
        secretOrKey: SECRET_KEY,
    }
    ```  
    </details>

3. <details>
    <summary>
    Using Custom Headers
    </summary>

    ```js
    // Client-side (e.g., using Axios)
    axios.get('/protected-resource', {
        headers: {
            'X-Custom-Header': token // Replace 'X-Custom-Header' with your custom header name
        }
    });

    // Custom extractor function for custom headers
    const customHeaderExtractor = (req) => {
        return req.headers['x-custom-header']; // Replace 'x-custom-header' with your custom header name
    };

    const opts = {
        jwtFromRequest: customHeaderExtractor, // Use custom extractor
        secretOrKey: SECRET_KEY,
    }
    ```
    </details>
