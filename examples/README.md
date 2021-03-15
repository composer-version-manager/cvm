# Summary

cd into the example folders to activate/deactivate cvm versions

## Simple

cd into the simple folder to activate composer 1.0.0

## nested000

cd into nested000 to activate composer 1.0.0
cd into nested000/nested001 to activate composer 1.0.1
cd into nested000/nested001/nested002 to activate composer 1.0.2

## nested100

cd into nested100 no change should happen
cd into nested100/nested101 to activate composer 1.0.0
cd into nested100/nested101/nested102, no change should happen. Should still use composer 1.0.0
cd into nested100/nested101/nested102/nested103 to activate composer 1.0.1
cd into nested100/nested101/nested102/nested103/nested104, No change should happen. Should still use composer 1.0.1
