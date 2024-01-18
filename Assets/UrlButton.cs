using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class UrlButton : MonoBehaviour
{
    public void OpenURL()
    {
        Application.OpenURL("https://www.google.com/");
    }
}
