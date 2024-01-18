#if CSHARP_7_3_OR_NEWER

// Licensed to the .NET Foundation under one or more agreements.
// The .NET Foundation licenses this file to you under the MIT license.
// See the LICENSE file in the project root for more information.

namespace Gpm.Common.ThirdParty.SharpCompress.Compressors.Deflate64
{
    internal enum MatchState
    {
        HasSymbol = 1,
        HasMatch = 2,
        HasSymbolAndMatch = 3
    }
}


#endif