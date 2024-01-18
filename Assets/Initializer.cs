using System.Collections;
using System.Collections.Generic;
using Google.XR.ARCoreExtensions.Samples.Geospatial;
using UnityEngine;

public class Initializer : MonoBehaviour
{
    private void Awake()
    {
        Debug.Log("krass");
        // Finde den GeospatialController im aktuellen Szenenkontext
        GeospatialController geospatialController = FindObjectOfType<GeospatialController>();

        // Überprüfe, ob der GeospatialController gefunden wurde
        if (geospatialController != null)
        {
            // Rufe die OnGetStarted-Funktion auf
            geospatialController.OnGetStartedClicked();
            Debug.Log("GeospatialController gefunden!");
        }
        else
        {
            Debug.LogError("GeospatialController nicht gefunden!");
        }
    }
}

