<img src="https://my-badges.github.io/my-badges/fix-6+.png" alt="I did 32 sequential fixes." title="I did 32 sequential fixes." width="128">
<strong>I did 32 sequential fixes.</strong>
<br><br>

Commits:

- <a href="https://github.com/kooked-ch/pictures/commit/bc15836a4df5fe7502166ec6e26d059f2f8be330">bc15836</a>: fix: Update join/page.tsx to handle user join request

The join/page.tsx file has been updated to handle user join requests by checking the validity of the provided token and the user's information. If the token is valid and the user's information is complete, they will be redirected to the home page. Otherwise, they will be redirected to the sign-in page. This change ensures a smooth and secure user join process.
- <a href="https://github.com/kooked-ch/pictures/commit/a281b9ed78690f42bba8aec35a519777def47915">a281b9e</a>: fix: Update layout to adjust main padding-top

The layout component has been updated to adjust the padding-top of the main content area. This change ensures proper spacing and alignment of the content, improving the overall visual appearance of the page.
- <a href="https://github.com/kooked-ch/pictures/commit/c9942db7aacaa5939815a56b896cf5874da7f536">c9942db</a>: fix: Update join page to handle user join request

The join page has been updated to handle user join requests by checking the validity of the provided token and the user's information. If the token is valid and the user's information is complete, they will be redirected to the home page. Otherwise, they will be redirected to the sign-in page. This change ensures a smooth and secure user join process.
- <a href="https://github.com/kooked-ch/pictures/commit/40003aec09f27fe0a51bb07650a28e3dc39ef2db">40003ae</a>: fix: Update phone number validation in signup page

The phone number validation in the signup page has been updated to check for a length of 12 digits instead of checking if it starts with '0'. This change ensures that only valid phone numbers are accepted during the signup process, improving data integrity and user experience.
- <a href="https://github.com/kooked-ch/pictures/commit/711708926b879f181e9e398e15e5d3133399a9f5">7117089</a>: fix: Update npm dependencies for net and tls packages

The npm dependencies for the 'net' and 'tls' packages have been updated to their latest versions. This change ensures that the application is using the most up-to-date and secure versions of these packages, improving overall stability and security.
- <a href="https://github.com/kooked-ch/pictures/commit/857d614a80199ade8f8e29ec736a5b2502f810dc">857d614</a>: fix: Update notifications table in init.sql

The 'notifications' table has been added to the 'init.sql' file. This change ensures that the database schema includes a table for storing notifications. The table has columns for 'notificationId', 'userId', 'message', 'link', 'type', 'isRead', and 'createdAt'. This addition allows the application to handle and display notifications to users, enhancing the user experience.
- <a href="https://github.com/kooked-ch/pictures/commit/8fc8b99ab2ca0a0e2c3d3ff273ba08732bb7a820">8fc8b99</a>: fix: Update variable name from 'name' to 'userName' in galleries.ts
- <a href="https://github.com/kooked-ch/pictures/commit/5abb48dbb2347a69b65f778c550390b1b84b5b32">5abb48d</a>: fix: Update birthday field in AccountForm component

The birthday field in the AccountForm component has been updated to use the value of 'undefined' instead of 'new Date()'. This change ensures consistency in handling the default value for the birthday field and improves code readability.
- <a href="https://github.com/kooked-ch/pictures/commit/7d09b995a87405c8ca86c3232a47e52ccd044803">7d09b99</a>: fix: Update variable name from 'phoneNum' to 'phoneNumber' in join/page.tsx
- <a href="https://github.com/kooked-ch/pictures/commit/9afc6e7d37ff2ce1ec36d4a4f6e7b198978aaeb6">9afc6e7</a>: fix: Update signup page to include phone number input

The signup page has been updated to include a phone number input field. This change allows users to enter their phone number during the signup process, ensuring that all necessary user information is captured and stored in the database. By including the phone number field, the application can provide a more comprehensive user profile and enhance the user experience.
- <a href="https://github.com/kooked-ch/pictures/commit/007b9d310d83c01995c2637fb323e112efb15678">007b9d3</a>: fix: Update join_gallery_requests table to use 'phoneNumber' column instead of 'phoneNum'

The 'join_gallery_requests' table in the database has been updated to use the 'phoneNumber' column instead of the 'phoneNum' column. This change ensures consistency and clarity in the naming convention for phone number fields across the database schema.
- <a href="https://github.com/kooked-ch/pictures/commit/e77afdd0d2efa40457aa4ae7856315ebb186fb03">e77afdd</a>: fix: Update signup route to include additional user fields

The signup route in 'route.ts' has been updated to include additional user fields such as 'lastname', 'username', and 'phoneNumber'. This change ensures that all necessary user information is captured during the signup process and stored in the database. By including these fields, the application can provide a more comprehensive user profile and enhance the user experience.
- <a href="https://github.com/kooked-ch/pictures/commit/c936de7fc54f9a6d115a466df2c073b54c52c92d">c936de7</a>: fix: Update variable name from 'phoneNum' to 'phoneNumber' in join/route.ts

The variable name 'phoneNum' has been updated to 'phoneNumber' in the 'join/route.ts' file. This change ensures consistency in variable naming and improves code readability.
- <a href="https://github.com/kooked-ch/pictures/commit/cb3445ee79607d2dfcc7a04de627f6563d465de3">cb3445e</a>: fix: Update variable name from 'name' to 'userName' in galleries.ts

The variable name 'name' has been updated to 'userName' in the 'galleries.ts' file. This change ensures consistency in variable naming and improves code readability.
- <a href="https://github.com/kooked-ch/pictures/commit/99cc16801f32d2c76a797b64e5f6d87868e5609d">99cc168</a>: fix: Update phoneNum to phoneNumber in join/input.tsx

The 'phoneNum' variable has been renamed to 'phoneNumber' in the 'join/input.tsx' file. This change ensures consistency in variable naming and improves code readability.
- <a href="https://github.com/kooked-ch/pictures/commit/088aba9e7828c6fc005194625aa8c13370ce36bd">088aba9</a>: fix: Update APP_DESCRIPTION in layout.tsx

The APP_DESCRIPTION in layout.tsx has been updated to 'Share your photos with friends and family'. This change improves the description of the application and provides a more accurate representation of its purpose.
- <a href="https://github.com/kooked-ch/pictures/commit/4c8af1ca8baf3a10ec9aa1b65977bc335d54685c">4c8af1c</a>: fix: Update background color style in otp.html

The background color style in otp.html has been updated to remove the min-height property and ensure consistency with the rest of the page. This change improves the visual appearance of the OTP page.
- <a href="https://github.com/kooked-ch/pictures/commit/465176916ef39fd46ced5041065a43d070168076">4651769</a>: fix: Update column name from 'phoneNum' to 'phoneNumber' in init.sql

The 'phoneNum' column name in the 'users' and 'join_gallery_requests' tables has been updated to 'phoneNumber' in the 'init.sql' file. This change ensures consistency and clarity in the naming convention for phone number fields across the database schema.
- <a href="https://github.com/kooked-ch/pictures/commit/b0213605866f3c5c64aa29a5699164422a290bc5">b021360</a>: fix: Update Dockerfile to run as root

The Dockerfile has been updated to change the user running the container from "nextjs" to "root". This change is necessary to allow the container to bind to port 80, which requires root privileges. By running the container as root, the application will be able to listen on port 80 and serve incoming requests.
- <a href="https://github.com/kooked-ch/pictures/commit/d1071b55c0f88964a515333d38b0fa97ea703c9e">d1071b5</a>: fix: Handle error saving file in upload route

The code changes in 'route.ts' now include error handling when saving a file. If an error occurs during the file saving process, an error message is logged to the console. This ensures that any errors encountered during file saving are properly handled and logged for debugging purposes.
- <a href="https://github.com/kooked-ch/pictures/commit/63856875279ebccedc49518f0105c0ab356045f9">6385687</a>: fix: Add email notification for new gallery creation

The code changes in 'galleries.ts' now include logic to send an email notification to the user when a new gallery is created. This ensures that the user is informed about the creation of their new gallery and provides them with a link to access it. The email content is generated from an HTML template file and includes the gallery's unique URL. This commit enhances the user experience by providing timely notifications for new gallery creations.
- <a href="https://github.com/kooked-ch/pictures/commit/4563833b3d725551001e3f4e1aaddce665a4a00b">4563833</a>: fix: Update Link href in GalleriesList component

The code changes in 'GalleriesList' component update the 'Link' href attribute to remove the '/edit' path. This ensures that the link correctly navigates to the gallery page instead of the edit page. The previous code included the '/edit' path, but it has been removed to align with the desired behavior.
- <a href="https://github.com/kooked-ch/pictures/commit/7178ffba4c1b6465db7f0ce2250cf951aec9f804">7178ffb</a>: fix: Update accreditation check in EditPage component

The code changes in 'EditPage' component now correctly check the 'userData.accreditationId' value to determine if the user has the correct accreditation to access the edit page for a specific gallery. The previous code used the value 3, but it has been updated to use the value 5. This ensures that only users with the correct accreditation can access the edit page.
- <a href="https://github.com/kooked-ch/pictures/commit/dfc76c03bc5315f231c5f6d46a0fbdf71647e322">dfc76c0</a>: fix: Redirect unauthorized users to '/me' in GalleryEditPage

The code changes in 'GalleryEditPage' now include a check for the 'userData.accreditationId' value. If the value is not equal to 5, the user is redirected to the '/me' page. This ensures that only users with the correct accreditation can access the edit page for a specific gallery.
- <a href="https://github.com/kooked-ch/pictures/commit/bd4327c7db3f5db2c75a44a2d9305cb83daa945f">bd4327c</a>: fix: Update getAccreditationId function to return 5 instead of 3

The code changes in users.ts update the getAccreditationId function to return 5 instead of 3 in a specific condition. This change ensures that the correct accreditation ID is returned based on the provided email and gallery ID.
- <a href="https://github.com/kooked-ch/pictures/commit/7510b64bc0c2bf95e9822e6a807a2ee74f459ff4">7510b64</a>: fix: Fix email sending in next-auth.ts

The code changes in next-auth.ts fix a bug in the email sending logic. The previous code was not correctly accessing the email address from the adminRows array, resulting in an error when trying to send the email. This commit updates the code to correctly access the email address and send the email to the admin user.
- <a href="https://github.com/kooked-ch/pictures/commit/0a4932cb3a1e1691aa1bcd994bbb284f8ce68598">0a4932c</a>: fix: Remove unused code in Page component
- <a href="https://github.com/kooked-ch/pictures/commit/eebd45592e379321a3a1fdf02194c26e01aebe9d">eebd455</a>: fix: Update email verification resend route
- <a href="https://github.com/kooked-ch/pictures/commit/b5f953aa6cb6b630219f766ae538ff4226505cb9">b5f953a</a>: fix: Update email verification resend route

The code changes in next-auth.ts add a new route for resending email verification. This allows users to request a new verification email if they did not receive the initial one or if it expired. This commit adds the necessary logic to handle the resend request and sends a new verification email to the user.
- <a href="https://github.com/kooked-ch/pictures/commit/81f1eff107fca454985783ed6297c702b5bbeb39">81f1eff</a>: fix: Correctly compare account provider in next-auth.ts
- <a href="https://github.com/kooked-ch/pictures/commit/3e893685da0a62f4ff2fe182cd00e3043fd90c07">3e89368</a>: fix: Correctly compare account provider in next-auth.ts

The code changes in next-auth.ts fix a logical error in the conditional statement that compares the account provider. The previous code did not correctly compare the provider, resulting in incorrect behavior. This commit updates the condition to ensure that the account provider is compared correctly before returning a value.
- <a href="https://github.com/kooked-ch/pictures/commit/ada14e9f288d31b927f5888f4c8a5a10892df2e7">ada14e9</a>: fix: Update conditional statement in next-auth.ts to correctly compare account provider

The code changes in next-auth.ts fix a logical error in the conditional statement that compares the account provider. The previous code did not correctly compare the provider, resulting in incorrect behavior. This commit updates the condition to ensure that the account provider is compared correctly before returning a value.


Created by <a href="https://github.com/my-badges/my-badges">My Badges</a>