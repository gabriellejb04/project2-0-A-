{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/gabriellejb04/project2-0-A-/blob/main/Project02A.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7tbqJGBD8-hW"
      },
      "source": [
        "<h1 style=\"margin-bottom: 0.4em; text-align: center;\">\n",
        "    <b>Project 02</b><br>\n",
        "    Assignment A\n",
        "</h1>\n",
        "<h2 style=\"margin-top: 0.0em; text-align: center;\">\n",
        "    Read mapping\n",
        "</h2>\n",
        "\n",
        "<p style=\"text-align: center;\">\n",
        "    <object hspace=\"50\">\n",
        "        <strong>Due</strong></a>: Mar 14, 2025 by 11:59 p.m.\n",
        "    </object>\n",
        "    <object hspace=\"50\">\n",
        "        <strong>Points</strong></a>: 100\n",
        "    </object>\n",
        "</p>\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "uBKKLaaL8-hZ"
      },
      "source": [
        "## Q01\n",
        "\n",
        "**Points:** 10\n",
        "\n",
        "In this part of the project, you will work with paired-end FASTQ reads from *Pseudomonas aeruginosa* biofilms grown under Ground and Space Day 3 conditions.\n",
        "The goal is to investigate how the bacteria responds to microgravity by analyzing gene expression data."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GAqYA5Kc8-ha"
      },
      "source": [
        "**Accessing data**\n",
        "\n",
        "Navigate to [this shared Galaxy project](https://usegalaxy.org/u/aalexmmaldonado/h/p02-data) that contains all necessary data for this project.\n",
        "You should see the following files:\n",
        "\n",
        "-   **ASM1462v1 Genes** : GFF3 file containing genes from the *Pseudomonas aeruginosa* strain used in the student.\n",
        "-   **ASM1462v1 rRNA** : FASTA file containing *Pseudomonas aeruginosa* rRNA sequences.\n",
        "-   **ASM1462v1** : Assembled *Pseudomonas aeruginosa* genome.\n",
        "-   **Space - Day 3 - FASTQ** : RNA-seq reads from *Pseudomonas aeruginosa* after three days on the International Space Station.\n",
        "-   **Ground - Day 3 - FASTQ** : RNA-seq reads from *Pseudomonas aeruginosa* after three days on the ground (i.e., control).\n",
        "\n",
        "Click the \"Import this history\" near the top of the screen and then click \"Copy History\".\n",
        "You only need to copy the active, non-deleted datasets.\n",
        "You will only be using this new Galaxy project for this assignment."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1873IOxj8-ha"
      },
      "source": [
        "**rRNA mapping**\n",
        "\n",
        "The objective of this step is to map your sequencing reads to a reference rRNA FASTA file, thereby identifying and filtering out ribosomal RNA sequences from your dataset.\n",
        "Ribosomal RNAs are highly abundant in total RNA samples, and if not removed, they can account for a large proportion of your sequencing data.\n",
        "This overwhelming presence can obscure the signals from messenger RNAs (mRNAs), which are crucial for understanding gene expression patterns.\n",
        "\n",
        "By mapping and subsequently removing rRNA sequences, you significantly enhance the quality and interpretability of your data.\n",
        "This process minimizes background noise, allowing for a more precise quantification of mRNA transcripts.\n",
        "Improved data clarity is essential for downstream analyses, such as differential gene expression, where accurate measurement of transcript levels is paramount.\n",
        "Moreover, eliminating rRNA contamination reduces computational load during analysis and contributes to more robust statistical conclusions.\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gIybMne48-hb"
      },
      "source": [
        "Begin by launching the Bowtie2 tool in Galaxy and configuring it as follows.\n",
        "For both the Space and Ground samples, you will run separate mappings for the forward and reverse paired-end reads.\n",
        "Follow these steps:\n",
        "\n",
        "1. **Library Type:**  \n",
        "   - Choose **\"paired\"** as your library type.\n",
        "2. **Input FASTQ Files:**  \n",
        "   - For each sample category, assign the forward and reverse FASTQ files to the appropriate input fields.  \n",
        "3. **Output Options:**  \n",
        "   - Enable the option to write unaligned reads to separate file(s) by setting it to **yes**.  \n",
        "   - Ensure that the option for writing aligned reads to separate files is set to **no**.\n",
        "4. **Reference Selection:**  \n",
        "   - Instead of using a built-in genome index, use a genome from the history and build index.\n",
        "   - Select the rRNA FASTA file (i.e., ASM1462v1) file as the reference.\n",
        "5. **Additional Settings:**  \n",
        "   - Do not set paired-end options.  \n",
        "   - Do not set read groups.  \n",
        "   - Do not tweak the analysis mode.\n",
        "   - Do not tweak SAM/BAM options.  \n",
        "   - Save the Bowtie2 mapping statistics to your history (set this option to **true**).\n",
        "6. **Execution:**  \n",
        "   - With all parameters set as specified, run the Bowtie2 mapping process for each sample condition (Space and Ground) separately.\n",
        "\n",
        "This configuration will align the paired-end reads from each sample to the rRNA reference, allowing you to filter out ribosomal RNA contamination."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "YtxDpguq8-hb"
      },
      "source": [
        "Once the Bowtie2 mapping process is completed, it's essential to carefully review the outputs in your Galaxy history to ensure that the alignment ran as expected.\n",
        "\n",
        "Locate the mapping statistics file generated by Bowtie2 in your Galaxy history.\n",
        "This file provides key performance metrics of your alignment, including the overall alignment rate, which is critical for assessing the quality of your mapping.\n",
        "Identify the percentage of reads that were successfully aligned to the rRNA reference.\n",
        "\n",
        "The variable `OVERALL_ALIGNMENT_RATE` is initially set to `0.0`.\n",
        "Replace this placeholder with the actual alignment rate reported in the mapping statistics.\n",
        "This value will be a benchmark for evaluating subsequent steps in your RNA-Seq analysis workflow."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "OaF3tVGL8-hc"
      },
      "outputs": [],
      "source": [
        "OVERALL_ALIGNMENT_RATE_GROUND = 49.27\n",
        "OVERALL_ALIGNMENT_RATE_SPACE = 19.8"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "The siginificance of the overall alignement rates shows how accurate or how successful the reads that align to a reference genome that we used. With these numbers in particular, the ground alignment rate, which is fairly moderatw shows that there is slight contamination, overall alignemnt rate for space is pretty poor and has a low alignment rate, which could be due to high contamination."
      ],
      "metadata": {
        "id": "USTCze_mK2S9"
      }
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GViNg9xh8-hd"
      },
      "source": [
        "\n",
        "---\n",
        "\n",
        "**Question** : Please comment on the meaning and significance of these values.\n",
        "\n",
        "PUT YOUR ANSWER HERE"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nKDrgCD88-hd"
      },
      "source": [
        "## Q02\n",
        "\n",
        "**Points:** 15\n",
        "\n",
        "In computational biology, read mapping is a crucial step in sequence alignment, where short DNA sequences (reads) are matched against a reference genome.\n",
        "One way to accelerate this process is by constructing a $k$-mer index, which serves as a lookup table for identifying potential matching regions in the reference genome.\n",
        "Instead of scanning the entire reference sequence for each query, we can use this index to efficiently locate potential seed matches.\n",
        "\n",
        "In this problem, you will implement a function, `build_kmer_index`, that constructs a hash table (Python dictionary) mapping each $k$-mer (subsequence of length $k$) to the list of positions where it appears in the reference genome.\n",
        "This index serves as the first step in seed-and-extend alignment algorithms, where we first locate potential matching regions before refining the alignment.\n",
        "\n",
        "**Why This Matters?**\n",
        "\n",
        "This indexing approach is fundamental in sequence alignment algorithms such as BLAST and Burrows-Wheeler Transform-based mappers.\n",
        "By precomputing locations of k-mers, we significantly speed up read alignment, making it feasible to process large genomic datasets.\n",
        "\n",
        "This problem will help students understand:\n",
        "- The importance of indexing in bioinformatics.\n",
        "- How to use Python data structures efficiently.\n",
        "- How preprocessing data (like creating a k-mer index) leads to faster searches in large datasets.\n",
        "\n",
        "**Programming Concepts Needed**\n",
        "\n",
        "To complete this task, students will apply the following Python concepts:\n",
        "\n",
        "1. Dictionaries (`dict`)\n",
        "   - We will use a dictionary to store k-mers as keys and their starting positions as values.\n",
        "   - Efficiently retrieving values from a dictionary allows quick lookups.\n",
        "2. Lists (`list`)\n",
        "   - Each dictionary key (a k-mer) maps to a list of positions, since a k-mer can occur multiple times in the reference sequence.\n",
        "3. For Loops (`for`)\n",
        "   - We iterate over the reference sequence to extract k-mers.\n",
        "   - The loop ensures that we capture every possible k-mer of length $k$.\n",
        "4. String Slicing (`str[start:end]`)\n",
        "   - Extracting a k-mer from the reference sequence using Python string slicing.\n",
        "5. Conditionals (`if-else`)\n",
        "   - Checking if a k-mer already exists in the dictionary to append to an existing list or create a new entry."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 55,
      "metadata": {
        "id": "aVoB2hmk8-he"
      },
      "outputs": [],
      "source": [
        "def build_kmer_index(reference: str, k: int) -> dict[str, list[int]]:\n",
        "    \"\"\"\n",
        "    Builds a hash table (i.e., dictionary) of k-mers from the reference sequence.\n",
        "\n",
        "    For each k-mer (substring of length k) in the reference, we record all starting\n",
        "    positions where the k-mer appears. This index will help us quickly look up\n",
        "    positions in the reference that match a k-mer from a query.\n",
        "\n",
        "    Args:\n",
        "        reference: The reference DNA sequence.\n",
        "        k: The length of k-mers to extract.\n",
        "\n",
        "    Returns:\n",
        "        A dictionary with k-mers as keys and a list of starting positions as values.\n",
        "\n",
        "    Examples:\n",
        "        >>> build_kmer_index(\"ATCGATCGA\", 3)\n",
        "        {'ATC': [0, 4], 'TCG': [1, 5], 'CGA': [2, 6], 'GAT': [3]}\n",
        "        >>> build_kmer_index(\"AAGGAA\", 2)\n",
        "        {'AA': [0, 4], 'AG': [1], 'GG': [2], 'GA': [3]}\n",
        "    \"\"\"\n",
        "\n",
        "    # TODO: Initialize an empty dictionary to hold k-mer positions.\n",
        "    k_mer_positions = {}\n",
        "    # TODO: Loop through the reference sequence.\n",
        "    for n in range(len(reference)-k+1):\n",
        "    # TODO: Extract the k-mer substring starting at the current index.\n",
        "      k_mer = reference[n:n+k]\n",
        "    # TODO: Check if the k-mer already exists in the dictionary.\n",
        "    # TODO: If it exists, append the current index to its list.\n",
        "    # TODO: If it does not exist, create a new list with the current index.\n",
        "      if k_mer not in k_mer_positions:\n",
        "        k_mer_positions[k_mer] = []\n",
        "      k_mer_positions[k_mer].append(n)\n",
        "    # TODO: Return the dictionary containing all k-mers and their positions.\n",
        "    return k_mer_positions"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "build_kmer_index(\"AAGGAA\", 2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8jupORkhEseR",
        "outputId": "879b633f-ccfc-4ab6-b501-fa312ed098d0"
      },
      "execution_count": 56,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'AA': [0, 4], 'AG': [1], 'GG': [2], 'GA': [3]}"
            ]
          },
          "metadata": {},
          "execution_count": 56
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NGCXX5Jz8-he"
      },
      "source": [
        "## Q03\n",
        "\n",
        "**Points:** 15\n",
        "\n",
        "Now that we've built a k-mer index, the next step is to use this index to efficiently identify candidate alignment start positions for a query sequence (short DNA read).\n",
        "Given a new read (query), we need to determine where in the reference genome we should start searching for an alignment.\n",
        "\n",
        "In traditional sequence alignment, an exhaustive search would compare the query against every possible position in the reference. However, by using a precomputed k-mer index, we can quickly vote on likely starting positions based on shared k-mers between the reference and query.\n",
        "\n",
        "Your task is to implement `map_query_to_reference`, a function that takes a query sequence, a precomputed k-mer index, and a k-mer length and returns a list of potential start positions where an alignment might begin.\n",
        "\n",
        "**Why This Matters?**\n",
        "\n",
        "- Many read mapping algorithms (like BLAST, BWA, and minimap2) first identify seed positions where an alignment is likely before performing more computationally expensive dynamic programming-based alignment (like Smith-Waterman).\n",
        "- A k-mer index allows us to quickly find regions of the reference that share exact substrings (k-mers) with the query, serving as potential alignment start points.\n",
        "- This process reduces the search space, making read mapping significantly faster.\n",
        "\n",
        "**Programming Concepts Needed**\n",
        "\n",
        "To complete this task, students will apply the following Python concepts:\n",
        "\n",
        "1. Dictionaries (`dict`)  \n",
        "   - The k-mer index is stored in a dictionary, mapping k-mers to their reference positions.\n",
        "   - Efficient key lookups allow quick retrieval of candidate positions.\n",
        "2. Lists (`list`)  \n",
        "   - A list is used to store candidate alignment positions.\n",
        "   - Removing duplicates ensures unique candidate positions.\n",
        "3. For Loops (`for`)  \n",
        "   - A loop slides a window of size k across the query sequence to extract k-mers.\n",
        "   - Another loop iterates over each reference position where a k-mer is found.\n",
        "4. String Slicing (`str[start:end]`)  \n",
        "   - Extracts k-mers from the query sequence.\n",
        "5. Conditionals (`if-else`)  \n",
        "   - Ensures only valid positions (non-negative) are included.\n",
        "   - Avoids duplicate entries by using a set.\n",
        "6. Sorting (`sorted()`)  \n",
        "   - Ensures candidate positions are returned in ascending order for consistency.\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 57,
      "metadata": {
        "id": "EvlXoOMS8-he"
      },
      "outputs": [],
      "source": [
        "def map_query_to_reference(\n",
        "    query: str, kmer_index: dict[str, list[int]], k: int\n",
        ") -> list[int]:\n",
        "    \"\"\"\n",
        "    Maps a query (read) to candidate alignment positions in the reference using the k-mer index.\n",
        "\n",
        "    For each k-mer in the query, if it exists in the k-mer index, we compute a potential\n",
        "    alignment start position by subtracting the k-mer's offset in the query from the k-mer's\n",
        "    position in the reference. This \"votes\" for a candidate alignment start position.\n",
        "\n",
        "    Args:\n",
        "        query: The query read sequence.\n",
        "        kmer_index: A dictionary mapping k-mers to lists of positions in the reference.\n",
        "        k: The k-mer length that was used to build the index.\n",
        "\n",
        "    Returns:\n",
        "        A sorted list of unique candidate alignment start positions in the reference.\n",
        "\n",
        "    Examples:\n",
        "        >>> kmer_dict = build_kmer_index(\"ATCGATCGA\", 3)\n",
        "        >>> map_query_to_reference(\"TCGA\", kmer_dict, 3)\n",
        "        [1, 5]\n",
        "        >>> kmer_dict = build_kmer_index(\"AAGGAAGGA\", 2)\n",
        "        >>> map_query_to_reference(\"GGA\", kmer_dict, 2)\n",
        "        [2, 6]\n",
        "        >>> map_query_to_reference(\"GGA\", kmer_dict, 4)\n",
        "        []\n",
        "    \"\"\"\n",
        "    # TODO: Initialize an empty list to store candidate alignment positions.\n",
        "    # TODO: Loop over the query sequence with a window of length k.\n",
        "    # Hint: Use range(len(query) - k + 1) to avoid index errors.\n",
        "    # TODO: Extract the current k-mer from the query using slicing.\n",
        "    # TODO: Check if the k-mer exists in the kmer_index.\n",
        "    # TODO: For each occurrence (position) of the k-mer in the reference,\n",
        "    # TODO: Compute the candidate alignment position (ref position minus current query index).\n",
        "    # TODO: Append the computed candidate position to your candidate positions list.\n",
        "\n",
        "    # TODO: Remove any duplicate candidate positions and filter out negative positions.\n",
        "    # Hints:\n",
        "    #   - Use a set to track which positions have been added.\n",
        "    #   - Only include positions that are non-negative.\n",
        "\n",
        "    # TODO: Return the sorted list of unique candidate alignment positions.\n",
        "    sol = []\n",
        "    for n in range(len(query) - k + 1):\n",
        "      k_mer = query[n:n+k]\n",
        "      if k_mer in kmer_index:\n",
        "        for pos in kmer_index[k_mer]:\n",
        "          align_pos = pos - n\n",
        "          if align_pos not in sol and align_pos > 0:\n",
        "            sol.append(align_pos)\n",
        "\n",
        "    return sol\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "kmer_dict = build_kmer_index(\"ATCGATCGA\", 3)\n",
        "map_query_to_reference(\"TCGA\", kmer_dict, 3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QG3UZWMrDgkv",
        "outputId": "a7c0c77e-041f-4bfa-cd52-d291eb1965b5"
      },
      "execution_count": 58,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 5]"
            ]
          },
          "metadata": {},
          "execution_count": 58
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ykTv0OPd8-hf"
      },
      "source": [
        "## Q04\n",
        "\n",
        "**Points:** 58\n",
        "\n",
        "The BWT is a fundamental data structure used in genomic sequence alignment and compression.\n",
        "It enables efficient searching, indexing, and compression of large DNA sequences.\n",
        "BWT is a critical component of tools like BWA and Bowtie, which are widely used for mapping sequencing reads to a reference genome.\n",
        "\n",
        "At a high level, BWT rearranges the input string in a way that groups similar characters together, making it highly compressible and enabling fast substring searches through FM-indexing. However, before we compute the BWT, we must ensure that the input text is properly formatted.\n",
        "\n",
        "\n",
        "The first function in our BWT pipeline is `prepare_text`. Before computing the BWT, we need to make sure the text contains a unique end marker (`$`).\n",
        "This marker helps us differentiate between different rotations of the string, ensuring that our suffix sorting is well-defined.\n",
        "Why is the `$` marker important?\n",
        "\n",
        "- Indicates the end of the string → Ensures that the transformation can be reversed.\n",
        "- Creates a unique suffix → Prevents ambiguity in suffix sorting.\n",
        "- Allows efficient alignment → Many bioinformatics algorithms rely on `$` for indexing genomic data.\n",
        "\n",
        "Your task is to implement `prepare_text`, which guarantees that any input string ends with a `$` marker.\n",
        "\n",
        "**Programming Concepts Needed**\n",
        "\n",
        "To complete this task, students will apply the following Python concepts:\n",
        "\n",
        "1. String Methods (`str.endswith()`)\n",
        "   - Used to check if the input already contains `$` at the end.\n",
        "2. String Concatenation (`+`)\n",
        "   - If the string does not end with `$`, we append it.\n",
        "3. Conditionals (`if-else`)\n",
        "   - Ensures we do not modify the string unnecessarily.\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 59,
      "metadata": {
        "id": "3R9fR3p48-hf"
      },
      "outputs": [],
      "source": [
        "test_str = \"bananas and bandanas are in the banana band\""
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 60,
      "metadata": {
        "id": "4MEk_KDm8-hf"
      },
      "outputs": [],
      "source": [
        "def prepare_text(text: str) -> str:\n",
        "    \"\"\"\n",
        "    Cleans the input text and ensures that it ends with a unique end marker '$'.\n",
        "\n",
        "    We do not handle the case if the original string ends in '$'.\n",
        "\n",
        "    Args:\n",
        "        text: The raw input string.\n",
        "\n",
        "    Returns:\n",
        "        The cleaned string that is guaranteed to end with '$'.\n",
        "\n",
        "    Examples:\n",
        "        >>> test_str = \"bananas and bandanas are in the banana band\"\n",
        "        >>> prepare_text(test_str)\n",
        "        bananas and bandanas are in the banana band$\n",
        "    \"\"\"\n",
        "    # TODO: Check if the input text ends with '$'.\n",
        "\n",
        "    # TODO: If the text does not end with '$', append '$' to the text.\n",
        "\n",
        "    # TODO: Return the cleaned text.\n",
        "\n",
        "\n",
        "    if '$' not in text:\n",
        "      text = text + '$'\n",
        "    return text\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "prepare_text(test_str)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "J_DdVhF701Eg",
        "outputId": "6623916f-47bf-4b9e-e2ca-d15a13694d34"
      },
      "execution_count": 61,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'bananas and bandanas are in the banana band$'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 61
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gG6Y-lOb8-hg"
      },
      "source": [
        "The Burrows-Wheeler Transform relies on a sorted list of all cyclic rotations of the input text.\n",
        "Each rotation is a version of the string where characters are cyclically shifted to the left.\n",
        "The key motivation behind this step is that sorting these rotations reveals patterns in the sequence that make substring searches faster.\n",
        "Why do we generate rotations?\n",
        "\n",
        "- Sorting these rotations is the foundation of BWT → The last column of the sorted rotations gives us the transformed text.\n",
        "- Reveals hidden structure in the sequence → Allows better compression and efficient searching.\n",
        "- Prepares the text for efficient FM-indexing, which is used in read alignment tools like BWA and Bowtie.\n",
        "\n",
        "Your task is to implement `generate_rotations`, which cyclically shifts the input text to create all possible rotations.\n",
        "\n",
        "**Programming Concepts Needed**\n",
        "\n",
        "To complete this task, students will apply the following Python concepts:\n",
        "\n",
        "1. String Concatenation (`+`)\n",
        "   - Construct cyclic rotations by shifting characters and combining substrings.\n",
        "2. String Slicing (`str[start:end]`)\n",
        "   - Used to extract substrings for creating rotations.\n",
        "3. Loops (`for`)\n",
        "   - Iterates through all possible shift positions to generate rotations.\n",
        "4. Lists (`list`)\n",
        "   - Stores and returns all generated rotations.\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 62,
      "metadata": {
        "id": "2_N3Gp8P8-hg"
      },
      "outputs": [],
      "source": [
        "def generate_rotations(text: str) -> list[str]:\n",
        "    \"\"\"\n",
        "    Generates all cyclic rotations of the input text.\n",
        "\n",
        "    Each rotation is created by taking a substring from the current index\n",
        "    to the end and concatenating it with the substring from the beginning\n",
        "    of the text up to the current index.\n",
        "\n",
        "    Args:\n",
        "        text: The input string.\n",
        "\n",
        "    Returns:\n",
        "        A list of all rotations of the text.\n",
        "\n",
        "    Examples:\n",
        "        >>> clean_str = \"bananas and bandanas are in the banana band$\"\n",
        "        >>> generate_rotations(clean_str)\n",
        "        [\n",
        "            'bananas and bandanas are in the banana band$',\n",
        "            'ananas and bandanas are in the banana band$b',\n",
        "            'nanas and bandanas are in the banana band$ba',\n",
        "            ...\n",
        "            'd$bananas and bandanas are in the banana ban',\n",
        "            '$bananas and bandanas are in the banana band'\n",
        "        ]\n",
        "    \"\"\"\n",
        "    # TODO: Initialize an empty list to store the rotations.\n",
        "\n",
        "    # TODO: Loop over the indices of the input text.\n",
        "\n",
        "    # TODO: For the current index i, create a rotation by concatenating\n",
        "    # the substring from i to the end with the substring from the beginning up to i.\n",
        "\n",
        "    # TODO: Append the generated rotation to the list.\n",
        "\n",
        "    # TODO: Return the list containing all rotations of the text.\n",
        "\n",
        "\n",
        "\n",
        "    rotations = []\n",
        "    for i in range(len(text)):\n",
        "     rotation = text[i:] + text[:i]\n",
        "     rotations.append(rotation)\n",
        "    return rotations\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "clean_str = \"bananas and bandanas are in the banana band$\"\n",
        "generate_rotations(clean_str)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "62TGhjfZ_AlM",
        "outputId": "eeb03610-36dd-44a1-cf43-20b4e221bdfb"
      },
      "execution_count": 63,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['bananas and bandanas are in the banana band$',\n",
              " 'ananas and bandanas are in the banana band$b',\n",
              " 'nanas and bandanas are in the banana band$ba',\n",
              " 'anas and bandanas are in the banana band$ban',\n",
              " 'nas and bandanas are in the banana band$bana',\n",
              " 'as and bandanas are in the banana band$banan',\n",
              " 's and bandanas are in the banana band$banana',\n",
              " ' and bandanas are in the banana band$bananas',\n",
              " 'and bandanas are in the banana band$bananas ',\n",
              " 'nd bandanas are in the banana band$bananas a',\n",
              " 'd bandanas are in the banana band$bananas an',\n",
              " ' bandanas are in the banana band$bananas and',\n",
              " 'bandanas are in the banana band$bananas and ',\n",
              " 'andanas are in the banana band$bananas and b',\n",
              " 'ndanas are in the banana band$bananas and ba',\n",
              " 'danas are in the banana band$bananas and ban',\n",
              " 'anas are in the banana band$bananas and band',\n",
              " 'nas are in the banana band$bananas and banda',\n",
              " 'as are in the banana band$bananas and bandan',\n",
              " 's are in the banana band$bananas and bandana',\n",
              " ' are in the banana band$bananas and bandanas',\n",
              " 'are in the banana band$bananas and bandanas ',\n",
              " 're in the banana band$bananas and bandanas a',\n",
              " 'e in the banana band$bananas and bandanas ar',\n",
              " ' in the banana band$bananas and bandanas are',\n",
              " 'in the banana band$bananas and bandanas are ',\n",
              " 'n the banana band$bananas and bandanas are i',\n",
              " ' the banana band$bananas and bandanas are in',\n",
              " 'the banana band$bananas and bandanas are in ',\n",
              " 'he banana band$bananas and bandanas are in t',\n",
              " 'e banana band$bananas and bandanas are in th',\n",
              " ' banana band$bananas and bandanas are in the',\n",
              " 'banana band$bananas and bandanas are in the ',\n",
              " 'anana band$bananas and bandanas are in the b',\n",
              " 'nana band$bananas and bandanas are in the ba',\n",
              " 'ana band$bananas and bandanas are in the ban',\n",
              " 'na band$bananas and bandanas are in the bana',\n",
              " 'a band$bananas and bandanas are in the banan',\n",
              " ' band$bananas and bandanas are in the banana',\n",
              " 'band$bananas and bandanas are in the banana ',\n",
              " 'and$bananas and bandanas are in the banana b',\n",
              " 'nd$bananas and bandanas are in the banana ba',\n",
              " 'd$bananas and bandanas are in the banana ban',\n",
              " '$bananas and bandanas are in the banana band']"
            ]
          },
          "metadata": {},
          "execution_count": 63
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "A-9Ixbp58-hg"
      },
      "source": [
        "Now that we have generated all cyclic rotations of our input text, the next step in the Burrows-Wheeler Transform is to sort these rotations lexicographically.\n",
        "However, we must handle a special case: The end-of-string marker `$` should always be considered the smallest character (i.e., it should sort before all other characters).\n",
        "\n",
        "This function, `bwt_sort_key`, defines a custom sorting key to ensure that when we sort rotations, `$` is always ranked lower than any other character.\n",
        "Why do we need a custom sorting key?\n",
        "\n",
        "- Lexicographic sorting is crucial → The structure of BWT relies on sorting the cyclic rotations of the input string.\n",
        "- Special handling of `$` → Since `$` is a non-alphabetic character, we need to ensure it sorts before any letter.\n",
        "- Facilitates fast FM-index searching → Sorting suffixes correctly is key to efficient substring searches.\n",
        "\n",
        "To achieve this, we create a tuple of numeric values where:\n",
        "\n",
        "- Characters are represented by their ASCII values (via `ord()`).\n",
        "- `$` is assigned a value of `-1`, ensuring it appears before any other character when sorted.\n",
        "\n",
        "**Programming Concepts Needed**\n",
        "\n",
        "To complete this task, students will apply the following Python concepts:\n",
        "\n",
        "1. ASCII Values (`ord()`)\n",
        "   - Converts characters into numeric ASCII values to be used as sorting keys.\n",
        "2. Conditionals (`if-else`)\n",
        "   - Ensures `$` is assigned a unique low value (`-1`).\n",
        "3. Lists (`list`)\n",
        "   - Stores the numeric representation of each character before converting to a tuple.\n",
        "4. Tuples (`tuple()`)\n",
        "   - Since sorting functions require immutable keys, the numeric list is converted into a tuple.\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 64,
      "metadata": {
        "id": "9vCvVP0a8-hg"
      },
      "outputs": [],
      "source": [
        "def bwt_sort_key(rotation: str) -> tuple[int]:\n",
        "    \"\"\"\n",
        "    Creates a sort key for a given rotation string, ensuring that the '$' character\n",
        "    is treated as smaller than all other ASCII characters.\n",
        "\n",
        "    This function iterates over each character in the rotation. If the character\n",
        "    is '$', it appends -1 to the key list (since -1 is less than any ASCII value).\n",
        "    Otherwise, it appends the ASCII value of the character using ord().\n",
        "\n",
        "    Args:\n",
        "        rotation: A rotation string from the Burrows-Wheeler Transform process.\n",
        "\n",
        "    Returns:\n",
        "        A tuple of numbers representing the sort key for the rotation.\n",
        "\n",
        "    Examples:\n",
        "        >>> test_str = \"bananas and bandanas are in the banana band$\"\n",
        "        >>>  bwt_sort_key(test_str)\n",
        "        (98, 97, 110, 97, ..., 110, 100, -1)\n",
        "    \"\"\"\n",
        "\n",
        "    # TODO: Initialize an empty list to store the key values.\n",
        "\n",
        "    # TODO: Iterate over each character in the input rotation string.\n",
        "    #   TODO: For each character, check if it is '$'.\n",
        "    #       TODO: If it is '$', append -1 to the key list.\n",
        "    #       TODO: Otherwise, append the ASCII value (obtained using ord()) of the character.\n",
        "\n",
        "    # TODO: Convert the list of key values into a tuple.\n",
        "\n",
        "    # TODO: Return the tuple as the sort key.\n",
        "\n",
        "\n",
        "    key_values = []\n",
        "\n",
        "    for char in rotation:\n",
        "      if char == '$':\n",
        "        key_values.append(-1)\n",
        "      else:\n",
        "        key_values.append(ord(char))\n",
        "\n",
        "    sort_key = tuple(key_values)\n",
        "    return sort_key\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "test_str = \"bananas and bandanas are in the banana band$\"\n",
        "bwt_sort_key(test_str)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Gbo5VjX1ErDw",
        "outputId": "7c28049b-257c-4df3-a9a8-fb98adca33b6"
      },
      "execution_count": 65,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(98,\n",
              " 97,\n",
              " 110,\n",
              " 97,\n",
              " 110,\n",
              " 97,\n",
              " 115,\n",
              " 32,\n",
              " 97,\n",
              " 110,\n",
              " 100,\n",
              " 32,\n",
              " 98,\n",
              " 97,\n",
              " 110,\n",
              " 100,\n",
              " 97,\n",
              " 110,\n",
              " 97,\n",
              " 115,\n",
              " 32,\n",
              " 97,\n",
              " 114,\n",
              " 101,\n",
              " 32,\n",
              " 105,\n",
              " 110,\n",
              " 32,\n",
              " 116,\n",
              " 104,\n",
              " 101,\n",
              " 32,\n",
              " 98,\n",
              " 97,\n",
              " 110,\n",
              " 97,\n",
              " 110,\n",
              " 97,\n",
              " 32,\n",
              " 98,\n",
              " 97,\n",
              " 110,\n",
              " 100,\n",
              " -1)"
            ]
          },
          "metadata": {},
          "execution_count": 65
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1YeHLTR_8-hg"
      },
      "source": [
        "Now that we have generated all cyclic rotations of our input text and defined a custom sorting key, the next step in the Burrows-Wheeler Transform process is to sort these rotations lexicographically. This is the key step that structures the transformation and prepares for efficient searching and compression.\n",
        "Why do we need to sort rotations?\n",
        "\n",
        "- The essence of the Burrows-Wheeler Transform is built on the idea of sorting all cyclic shifts of the input text.\n",
        "- By sorting these shifts, we create a structured representation of the text that allows faster searching and compression.\n",
        "- The sorted rotations help identify patterns in the sequence, which is fundamental for FM-index-based read mapping.\n",
        "\n",
        "This function, `sort_rotations`, takes in a list of rotations and sorts them using our previously defined sorting key (`bwt_sort_key`), ensuring that the `$` marker appears first.\n",
        "\n",
        "**Programming Concepts Needed**\n",
        "\n",
        "To complete this task, students will apply the following Python concepts:\n",
        "\n",
        "1. Sorting (`sorted()`)\n",
        "   - Uses Python’s built-in sorting function to arrange rotations.\n",
        "2. Custom Sorting Key (`key=function`)\n",
        "   - Applies the previously implemented `bwt_sort_key` function to handle the special ordering of `$`."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 80,
      "metadata": {
        "id": "kbBmVXW18-hh"
      },
      "outputs": [],
      "source": [
        "def sort_rotations(rotations: list[str]) -> list[str]:\n",
        "    \"\"\"\n",
        "    Sorts the list of rotations in lexicographical order,\n",
        "    ensuring that the '$' character is treated as smaller than all other ASCII characters.\n",
        "\n",
        "    Args:\n",
        "        rotations: A list of rotations (strings).\n",
        "\n",
        "    Returns:\n",
        "        A list of rotations sorted according to the custom key.\n",
        "    \"\"\"\n",
        "    # TODO: Sort the list of rotations using the custom key function bwt_sort_key.\n",
        "\n",
        "    # TODO: Return the sorted list of rotations.\n",
        "\n",
        "    return sorted(rotations, key=bwt_sort_key)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Uu1vZEqw8-hh"
      },
      "source": [
        "Now that we have sorted all cyclic rotations of the input text, we can finally construct the Burrows-Wheeler Transform.\n",
        "This is done by extracting the last column from the sorted rotations.\n",
        "Why do we extract the last column?\n",
        "\n",
        "- The last column of the sorted cyclic rotations is the key to the Burrows-Wheeler Transform.\n",
        "- The BWT rearranges the original string into a highly compressible form by grouping similar characters together.\n",
        "- This transformation allows for fast substring searches using the FM-index, which is widely used in genomic sequence alignment.\n",
        "\n",
        "By extracting the last character of each sorted rotation, we obtain the BWT of the original input text.\n",
        "\n",
        "**Programming Concepts Needed**\n",
        "\n",
        "To complete this task, students will apply the following Python concepts:\n",
        "\n",
        "1. String Indexing (`str[-1]`)\n",
        "   - Retrieves the last character of each sorted rotation.\n",
        "2. Lists (`list`)\n",
        "   - Stores last characters before converting them into a string.\n",
        "3. Looping (`for`)\n",
        "   - Iterates through each sorted rotation to extract the last column.\n",
        "4. String Joining (`\"\".join()`)\n",
        "   - Efficiently combines characters into the final BWT string.\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 81,
      "metadata": {
        "id": "UcAQ2K3Y8-hh"
      },
      "outputs": [],
      "source": [
        "def extract_last_column(sorted_rotations: list[str]) -> str:\n",
        "    \"\"\"\n",
        "    Extracts the last character from each rotation to form the BWT string.\n",
        "\n",
        "    Args:\n",
        "        sorted_rotations: The sorted list of rotations.\n",
        "\n",
        "    Returns:\n",
        "        The BWT of the original string.\n",
        "\n",
        "    Examples:\n",
        "        >>> extract_last_column(sorted_rotations)\n",
        "        'dsseadennnbbndb b nn $  nnnhrt iaaaaaaaaaaa '\n",
        "    \"\"\"\n",
        "    # TODO: Initialize an empty list to store the last characters from each rotation.\n",
        "\n",
        "    # TODO: Loop over each rotation in the sorted_rotations list.\n",
        "    # TODO: Extract the last character of the current rotation.\n",
        "    # TODO: Append the extracted character to the list of last characters.\n",
        "\n",
        "    # TODO: Combine the list of last characters into a single string.\n",
        "\n",
        "    # TODO: Return the resulting string (the BWT of the original text).\n",
        "\n",
        "\n",
        "    last_characters = []\n",
        "    for rotation in sorted_rotations:\n",
        "      last_char = rotation[-1]\n",
        "      last_characters.append(last_char)\n",
        "\n",
        "    return ''.join(last_characters)\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "extract_last_column(sorted_rotations)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "AyrWWborOPfd",
        "outputId": "eda9af8f-707e-4eaf-b1d5-3b5463933c4e"
      },
      "execution_count": 84,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'dsseadennnbbndb b nn $  nnnhrt iaaaaaaaaaaa '"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 84
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "iommr9X5YQzX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "98QCx8pROPXG"
      }
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "P3CuPJFPOPBw"
      }
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "c2q9qWy58-hh"
      },
      "source": [
        "## Q05\n",
        "\n",
        "**Points:** 2\n",
        "\n",
        "Building on our introduction to the BWT, we now turn to an essential step in reconstructing the original string or aligning reads using LF-mapping.\n",
        "In the context of read mapping, once we have compressed the reference sequence via the BWT, we often want to efficiently locate where a given read might match.\n",
        "LF-mapping is central to this process because it tells us, for each character in the BWT (the “last column”), which row and character in the first column it corresponds to.\n",
        "By repeatedly applying LF-mapping, we can recover the positions in the original string or track how short reads align."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 85,
      "metadata": {
        "id": "r1plgE3k8-hh"
      },
      "outputs": [],
      "source": [
        "test_bwt = \"dsseadennnbbndb b nn $  nnnhrt iaaaaaaaaaaa \""
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-neY12g_8-hh"
      },
      "source": [
        "However, to perform LF-mapping, we first need to construct the so-called “first column,” which lists the same characters found in the BWT but in sorted order.\n",
        "This sorting step is crucial because it re-establishes the lexicographic relationships among the characters that were disrupted by the transform.\n",
        "By knowing the positions of characters in the first column, we can track exactly which occurrence of each character in the BWT corresponds to each occurrence in the sorted first column.\n",
        "\n",
        "From a programming standpoint, this function is a straightforward exercise in string manipulation and sorting in Python:\n",
        "\n",
        "- You will work with a string (the BWT) and transform it by applying the built-in sorted function, which returns a list of characters sorted in ascending order.  \n",
        "- You will then join these sorted characters back together into a single string to form the first column.  \n",
        "- This highlights the use of Python’s core data structures—specifically, lists for intermediate sorting—and the string operations available to compose your final output.  \n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 91,
      "metadata": {
        "id": "PXFJu0mC8-hi"
      },
      "outputs": [],
      "source": [
        "def create_first_column(bwt: str) -> str:\n",
        "    \"\"\"\n",
        "    Given a BWT, construct the 'first column' by sorting the characters in BWT.\n",
        "\n",
        "    Args:\n",
        "        bwt: The Burrows-Wheeler Transform string.\n",
        "\n",
        "    Returns:\n",
        "        A string representing the sorted characters of the BWT (the first column).\n",
        "\n",
        "    Examples:\n",
        "        >>> test_bwt = \"dsseadennnbbndb b nn $  nnnhrt iaaaaaaaaaaa \"\n",
        "        >>> create_first_column(test_bwt)\n",
        "        '$       aaaaaaaaaaaabbbbdddeehinnnnnnnnnrsst'\n",
        "    \"\"\"\n",
        "    # TODO: Sort the characters in the BWT using the custom sort key bwt_sort_key.\n",
        "    # Hint: Use Python's built-in sorted() function and join the characters to form a string.\n",
        "\n",
        "    # TODO: Return the sorted string (the first column).\n",
        "    return sorted(bwt, key=bwt_sort_key)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "test_bwt = \"dsseadennnbbndb b nn $  nnnhrt iaaaaaaaaaaa \"\n",
        "create_first_column(test_bwt)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "U4NjBim5dT1B",
        "outputId": "d6e63b9c-bbb6-446d-e666-b34bfbe797fc"
      },
      "execution_count": 92,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['$',\n",
              " ' ',\n",
              " ' ',\n",
              " ' ',\n",
              " ' ',\n",
              " ' ',\n",
              " ' ',\n",
              " ' ',\n",
              " 'a',\n",
              " 'a',\n",
              " 'a',\n",
              " 'a',\n",
              " 'a',\n",
              " 'a',\n",
              " 'a',\n",
              " 'a',\n",
              " 'a',\n",
              " 'a',\n",
              " 'a',\n",
              " 'a',\n",
              " 'b',\n",
              " 'b',\n",
              " 'b',\n",
              " 'b',\n",
              " 'd',\n",
              " 'd',\n",
              " 'd',\n",
              " 'e',\n",
              " 'e',\n",
              " 'h',\n",
              " 'i',\n",
              " 'n',\n",
              " 'n',\n",
              " 'n',\n",
              " 'n',\n",
              " 'n',\n",
              " 'n',\n",
              " 'n',\n",
              " 'n',\n",
              " 'n',\n",
              " 'r',\n",
              " 's',\n",
              " 's',\n",
              " 't']"
            ]
          },
          "metadata": {},
          "execution_count": 92
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "u94AKnFI8-hi"
      },
      "source": [
        "Once we have created the sorted list of characters (i.e., the first column) from our BWT, we need an efficient way to locate the exact row where each character first appears in this column.\n",
        "Tracking these *first occurrences* is important for reconstructing the original string or aligning reads using LF-mapping because it tells us the offset in the first column for any character in the BWT.\n",
        "By knowing exactly where each character starts, we can map occurrences of that character in the BWT (the “last column”) back to the correct position in the first column.\n",
        "\n",
        "In practical terms, if we encounter a certain character at position $i$ in the BWT, we will need to know where that character’s block begins in the first column to calculate how many times it has appeared up to that point.\n",
        "This “first occurrence” dictionary provides that starting index for every character.\n",
        "\n",
        "Your task is to write a function that, given the first column string, computes a dictionary that maps every character in the first column to the index of its first occurrence.\n",
        "You will:\n",
        "\n",
        "- Iterate over the characters in the first column.\n",
        "- For each character, if it has not yet been added to the dictionary, store its current index.\n",
        "- Return the completed dictionary.\n",
        "\n",
        "This function is another critical step in our LF-mapping pipeline, as we will ultimately use the returned dictionary to navigate through the BWT’s rows when reconstructing or aligning reads.\n",
        "\n",
        "**Programming Concepts Needed**\n",
        "\n",
        "- You will use a Python dictionary to map each character to its first occurrence index.\n",
        "- You will iterate through the first column once, which is an O(n) operation where n is the length of the string.\n",
        "- A simple `if char not in dict` check ensures each character is recorded only once.\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "JuWHBO-K8-hi"
      },
      "outputs": [],
      "source": [
        "def compute_first_occurrence(first_col: str) -> dict[str, int]:\n",
        "    \"\"\"\n",
        "    Compute the position of the first occurrence of each character in the first column.\n",
        "\n",
        "    Args:\n",
        "        first_col: The first column (sorted characters of BWT).\n",
        "\n",
        "    Returns:\n",
        "        A dictionary mapping each character to its first occurrence index in `first_col`.\n",
        "\n",
        "    Examples:\n",
        "        >>> test_bwt = \"dsseadennnbbndb b nn $  nnnhrt iaaaaaaaaaaa \"\n",
        "        >>> first_column = create_first_column(test_bwt)\n",
        "        >>> compute_first_occurrence(first_column)\n",
        "        {\n",
        "            '$': 0,\n",
        "            ' ': 1,\n",
        "            'a': 8,\n",
        "            'b': 20,\n",
        "            'd': 24,\n",
        "            'e': 27,\n",
        "            'h': 29,\n",
        "            'i': 30,\n",
        "            'n': 31,\n",
        "            'r': 40,\n",
        "            's': 41,\n",
        "            't': 43\n",
        "        }\n",
        "\n",
        "        Imagine your first column is generated from a BWT that includes the characters\n",
        "        `['$', ' ', 'a', 'a', 'b', ...]`. If `$` appears first, then `'$': 0` will be\n",
        "        added to the dictionary. Once the code sees a new character like `'a'` at\n",
        "        index 2, it records `'a': 2`. When it encounters another `'a'` later,\n",
        "        it ignores it because `'a'` is already in the dictionary.\n",
        "    \"\"\"\n",
        "    # TODO: Initialize an empty dictionary to store the first occurrence positions.\n",
        "\n",
        "    # TODO: Iterate over the characters in first_col with their index.\n",
        "    # Hint: Use the enumerate() function.\n",
        "    # TODO: For each character, check if it is not already present in the dictionary.\n",
        "    # TODO: If it is not present, assign the current index as its value.\n",
        "\n",
        "    # TODO: Return the dictionary with the first occurrence of each character.\n",
        "\n",
        "\n",
        "    occurrence_positions = {}\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KmzhusR18-hi"
      },
      "source": [
        "After computing the first occurrence dictionary and obtaining the BWT string, the next critical step is to implement the backward search algorithm.\n",
        "This algorithm allows us to quickly identify all positions (i.e., rows) in the BWT where a given search pattern occurs.\n",
        "In a nutshell, backward search begins with the full range of the BWT and refines it by processing the pattern in reverse—from the last character to the first.\n",
        "For each character in the pattern, we update the range using two key pieces of information:\n",
        "\n",
        "- First Occurrence tells us where the block of a particular character starts in the sorted first column.\n",
        "- By counting how many times the character has appeared in the BWT up to certain positions, we adjust our search range accordingly by using the occurrence count.\n",
        "\n",
        "By iteratively narrowing down the range (defined by the `top` and `bottom` indices), backward search eventually isolates a contiguous block in the BWT where the entire pattern is present.\n",
        "If at any point the range becomes invalid (i.e., `top` exceeds `bottom`), it indicates that the pattern does not exist within the BWT.\n",
        "\n",
        "Your task is to write a function that performs this backward search.\n",
        "Given the BWT string, the search pattern, and the first occurrence dictionary, the function should:\n",
        "\n",
        "- Initialize the search range to cover the entire BWT.\n",
        "- Iterate through the pattern in reverse order.\n",
        "- For each character, update the `top` and `bottom` indices by:\n",
        "    - Determining the starting index of the character in the first column using the dictionary.\n",
        "    - Counting the occurrences of the character up to the current `top` and `bottom` indices.\n",
        "- Return the list of row indices (from `top` to `bottom`) where the pattern is found.\n",
        "- Return an empty list if the pattern is not present (i.e., when the search range becomes invalid).\n",
        "\n",
        "This backward search function is a key component in various string-matching and bioinformatics applications, such as reconstructing the original string from its BWT or aligning sequencing reads efficiently.\n",
        "\n",
        "**Programming Concepts Needed**\n",
        "\n",
        "- Index Manipulation: Handling the `top` and `bottom` indices that define the current search range.\n",
        "- Reverse Iteration: Traversing the pattern from end to start to progressively refine the range.\n",
        "- Counting Occurrences: Using simple counting (or more advanced techniques for larger datasets) to determine the number of times a character appears up to a certain index in the BWT.\n",
        "- Conditional Checks: Ensuring the search range remains valid throughout the process."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "veItVHKZ8-hi"
      },
      "outputs": [],
      "source": [
        "def backward_search(\n",
        "    bwt: str, pattern: str, first_occurrence: dict[str, int]\n",
        ") -> list[int]:\n",
        "    \"\"\"\n",
        "    Find all rows in the BWT where 'pattern' occurs via the backward search algorithm.\n",
        "    This version returns a list of row indices [top, top+1, ..., bottom].\n",
        "\n",
        "    Args:\n",
        "        bwt: The Burrows-Wheeler Transform string.\n",
        "        pattern: The substring to search for.\n",
        "        first_occurrence: Dictionary mapping a character to its first occurrence index in\n",
        "            the sorted first column (e.g., {'$':0, 'a':1, 'b':4, ...}).\n",
        "\n",
        "    Returns:\n",
        "        A list of row indices in the BWT that match 'pattern'.\n",
        "            If no occurrences are found, this list is empty.\n",
        "\n",
        "    Examples:\n",
        "        >>> test_str = \"bananas and bandanas are in the banana band\"\n",
        "        >>> test_bwt = \"dsseadennnbbndb b nn $  nnnhrt iaaaaaaaaaaa \"\n",
        "        >>> search_str = \"ban\"\n",
        "        >>> first_column = create_first_column(test_bwt)\n",
        "        >>> first_occ = compute_first_occurrence(first_column)\n",
        "        >>> backward_search(test_bwt, search_str, first_occ)\n",
        "        [20, 21, 22, 23]\n",
        "    \"\"\"\n",
        "    # TODO: Initialize 'top' to 0 and 'bottom' to len(bwt) - 1.\n",
        "\n",
        "    # TODO: Loop over the pattern from the last character to the first character.\n",
        "    # Hint: Use a loop like: for i in range(len(pattern) - 1, -1, -1)\n",
        "    #   TODO: Extract the current symbol from the pattern.\n",
        "\n",
        "    #   TODO: Check if the current symbol is not in first_occurrence.\n",
        "    #         If it's not, return an empty list (no matches found).\n",
        "\n",
        "    #   TODO: Count the number of occurrences of the symbol in bwt from the start up to 'top'.\n",
        "    #         Hint: Use bwt[:top].count(symbol)\n",
        "\n",
        "    #   TODO: Count the number of occurrences of the symbol in bwt from the start up to 'bottom + 1'.\n",
        "    #         Hint: Use bwt[:bottom + 1].count(symbol)\n",
        "\n",
        "    #   TODO: Update 'top' to be first_occurrence[symbol] plus the count from bwt[:top].\n",
        "    #   TODO: Update 'bottom' to be first_occurrence[symbol] plus the count from bwt[:bottom + 1] minus 1.\n",
        "\n",
        "    #   TODO: If the updated 'top' is greater than 'bottom', return an empty list as no match exists.\n",
        "\n",
        "    # TODO: After processing all characters of the pattern, return a list of indices from 'top' to 'bottom' (inclusive).\n",
        "    # Hint: Use range(top, bottom + 1) to generate the list of row indices."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "drEzQljd8-hj"
      },
      "source": [
        "LF-mapping is the operation that links each character in the BWT “last column” to its corresponding position in the “first column.” By pairing a character with its *rank*—that is, which occurrence of that character it is in the BWT from left to right—you can pinpoint the exact row in the full BWT matrix where that character belongs.\n",
        "This process is essential for reconstructing the original string from the BWT or for aligning reads quickly against a reference in advanced alignment algorithms.\n",
        "\n",
        "When traversing the BWT, you will repeatedly ask, “Given this character and how many times we have seen it so far (its rank), which row and character in the first column does this correspond to?” Specifically, for each `(character, rank)` pair in the BWT, it tracks the row index at which that pair appears.\n",
        "Later, you will combine this with your `first_occurrence` information to jump back and forth between the last and first columns (an essential step in full reconstruction or read alignment).\n",
        "\n",
        "**Programming Concepts Needed**\n",
        "\n",
        "- You will loop through each position `i` in the BWT (e.g., using `for i, char in enumerate(bwt):`).  \n",
        "- A dictionary called `lf_map` will map `(char, rank)` pairs to row indices. This requires you to use tuples `(char, rank)` as keys.  \n",
        "- You will maintain a separate dictionary (`char_count`) that tracks how many times each character has appeared so far. This uses basic dictionary get-or-initialize logic.  \n",
        "- Storing `(char, rank)` as a key demonstrates how Python supports composite keys in dictionaries.  "
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "a7_Oir0k8-hj"
      },
      "outputs": [],
      "source": [
        "def compute_lf_mapping(bwt: str) -> dict[tuple[str, int], int]:\n",
        "    \"\"\"\n",
        "    Compute the LF-mapping, which maps (character, rank) in BWT\n",
        "    to its position in the first column.\n",
        "\n",
        "    Args:\n",
        "        bwt: The Burrows-Wheeler Transform string.\n",
        "\n",
        "    Returns:\n",
        "        A dictionary where the key is (character, rank_in_bwt) and\n",
        "        the value is the index in the first column where that\n",
        "        (character, rank_in_bwt) pair is found.\n",
        "\n",
        "    Examples:\n",
        "        >>> test_bwt = \"dsseadennnbbndb b nn $  nnnhrt iaaaaaaaaaaa \"\n",
        "        >>> compute_lf_mapping(test_bwt)\n",
        "        {\n",
        "            ('d', 0): 0,\n",
        "            ('s', 0): 1,\n",
        "            ('s', 1): 2,\n",
        "            ('e', 0): 3,\n",
        "            ...\n",
        "            ('a', 10): 41,\n",
        "            ('a', 11): 42,\n",
        "            (' ', 6): 43\n",
        "        }\n",
        "\n",
        "    \"\"\"\n",
        "    # TODO: Initialize an empty dictionary to keep track of the count of each character.\n",
        "\n",
        "    # TODO: Initialize an empty dictionary for the LF-mapping.\n",
        "\n",
        "    # TODO: Loop over the indices and characters of the bwt string using enumerate().\n",
        "    #   TODO: If the character hasn't been seen before, initialize its count to 0.\n",
        "    #   TODO: Create a key as a tuple (character, current count) representing its rank.\n",
        "    #   TODO: Map this key to the current index in the LF-mapping dictionary.\n",
        "    #   TODO: Increment the count for this character.\n",
        "\n",
        "    # TODO: Return the completed LF-mapping dictionary."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "iFxblyD38-hj"
      },
      "source": [
        "After running `backward_search` to find the matching row indices in the BWT, you often want to get each match’s starting position in the *original* text (not just the row in the BWT).\n",
        "To do this, you can walk backward from a given row to the sentinel character (e.g., `'$'`) in the BWT, counting how many steps it takes.\n",
        "That step count is effectively the *suffix array index*—the starting position of that matching suffix in the original text.\n",
        "\n",
        "The function `get_suffix_indices_for_matches` accomplishes this by building an inverse of your `lf_map` so you can quickly go from “row index” back to “(char, rank).”\n",
        "Each step in this backward walk lets you track one character earlier in the original string, until you finally reach the sentinel.\n",
        "\n",
        "**Programming Concepts Needed**\n",
        "\n",
        "- You must invert the LF map (which goes `(char, rank) -> row_index`) into a structure that answers `row_index -> (char, rank)`.  \n",
        "- A `while` loop continues walking backward until it encounters the sentinel (`'$'`), at which point it stops.  \n",
        "- Like LF mapping, the inverse uses tuples `(char, rank)` as dictionary keys, but here you also store them as dictionary values to allow the reverse lookup.  \n",
        "- You maintain a counter (`steps`) to count how many backward steps you take, which equates to the position offset in the original string.  \n",
        "- The function processes each matching row from `backward_search` in turn, generating a final list of suffix positions in the original text."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "reDr4W3p8-hj"
      },
      "outputs": [],
      "source": [
        "def get_suffix_indices_for_matches(\n",
        "    bwt: str,\n",
        "    matched_rows: list[int],\n",
        "    first_occurrence: dict[str, int],\n",
        "    lf_map: dict[tuple[str, int], int],\n",
        ") -> list[int]:\n",
        "    \"\"\"\n",
        "    Given a list of rows in the BWT that match a pattern, determine each matching\n",
        "    suffix's starting position in the original text by walking backward to the sentinel.\n",
        "\n",
        "    Args:\n",
        "        bwt: The Burrows-Wheeler Transform string of the original text,\n",
        "             which must contain a unique sentinel (e.g., '$').\n",
        "        matched_rows: A list of row indices in the BWT that match a pattern\n",
        "            (e.g., from the backward_search function).\n",
        "        first_occurrence: Dictionary mapping each character to its first occurrence\n",
        "            index in the first column.\n",
        "        lf_map: Dictionary mapping (char, rank_in_bwt) to the row index in the first column.\n",
        "                For example, {('a', 0): 5, ('a', 1): 6, ...}.\n",
        "\n",
        "    Returns:\n",
        "        A list of integers representing the starting positions of each matching suffix\n",
        "            in the original text. The i-th element of the list corresponds to the\n",
        "            i-th element of matched_rows.\n",
        "\n",
        "    Examples:\n",
        "        >>> test_str = \"bananas and bandanas are in the banana band\"\n",
        "        >>> test_bwt = \"dsseadennnbbndb b nn $  nnnhrt iaaaaaaaaaaa \"\n",
        "        >>> row_matches = backward_search(test_bwt, search_str, first_occ)\n",
        "        >>> first_column = create_first_column(test_bwt)\n",
        "        >>> first_occ = compute_first_occurrence(first_column)\n",
        "        >>> lf_map = compute_lf_mapping(test_bwt)\n",
        "        >>> get_suffix_indices_for_matches(test_bwt, row_matches, first_occ, lf_map)\n",
        "        [32, 0, 39, 12]\n",
        "\n",
        "    Notes:\n",
        "        This function constructs the 'inverse LF-map' so that we can go from\n",
        "        row -> (char, rank). Once we have (char, rank), we use:\n",
        "\n",
        "        ```python\n",
        "        new_row = first_occurrence[char] + rank\n",
        "        ```\n",
        "\n",
        "        to jump back one character in the original rotation.\n",
        "\n",
        "        The total number of such backward steps to reach '$' is exactly the\n",
        "        suffix's starting position in the original text (assuming the sentinel marks\n",
        "        the beginning of the text).\n",
        "    \"\"\"\n",
        "    # TODO: Build the inverse mapping of lf_map so that you can go from row index -> (char, rank).\n",
        "\n",
        "    # TODO: Initialize an empty list to store the starting positions of each suffix.\n",
        "\n",
        "    # TODO: Iterate over each row in matched_rows.\n",
        "    # TODO: Initialize a counter for the number of backward steps.\n",
        "    # TODO: While the character in bwt at the current row is not the sentinel '$':\n",
        "    # TODO: Retrieve the (char, rank) corresponding to the current row using the inverse mapping.\n",
        "    # TODO: Update row by computing the new row: first_occurrence[char] + rank.\n",
        "    # TODO: Increment the steps counter.\n",
        "    # TODO: After reaching the sentinel, append the number of steps to the list of positions.\n",
        "\n",
        "    # TODO: Return the list of starting positions."
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "default",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.12.8"
    },
    "colab": {
      "provenance": [],
      "include_colab_link": true
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}