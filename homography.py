import cv2
import numpy as np  


img1 = cv2.imread("paper.webp")
img2 = cv2.imread("distorted_image.jpg")


img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


orb = cv2.ORB_create(50)


kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None) 


img3 = cv2.drawKeypoints(img1, kp1, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
img4 = cv2.drawKeypoints(img2, kp2, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)


matches = matcher.knnMatch(des1, des2, k=2)


good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:  # Lowe's ratio test
        good_matches.append(m)

good_matches = sorted(good_matches, key=lambda x: x.distance)

print(f'Number of good matches: {len(good_matches)}')


point1 = np.zeros((len(matches),2), dtype=np.float32)
point2 = np.zeros((len(matches),2), dtype=np.float32)

for i, match in enumerate(matches):
    match=match[0]
    point1[i, :] = kp1[match.queryIdx].pt
    point2[i, :]=  kp2[match.trainIdx].pt

print(point1)
print(point2)

img_matches = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)


h,  mask = cv2.findHomography(point1, point2, cv2.RANSAC)
print(h)

height , width = img2.shape

newimage = cv2.warpPerspective(img1,h,(width,height))

cv2.imshow('Keypoints Image 1', newimage)
#cv2.imshow('Keypoints Image 2', img4)
#cv2.imshow('Matches', img_matches)

cv2.waitKey(0)
cv2.destroyAllWindows()