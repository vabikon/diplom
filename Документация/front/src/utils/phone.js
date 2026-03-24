export function formatRussianPhone(value = "") {
  const digits = String(value).replace(/\D/g, "");
  const normalized = digits.startsWith("7")
    ? digits.slice(1)
    : digits.startsWith("8")
    ? digits.slice(1)
    : digits;
  const limited = normalized.slice(0, 10);

  if (!limited.length) {
    return "";
  }

  let formatted = "+7";

  if (limited.length > 0) {
    formatted += ` (${limited.slice(0, 3)}`;
  }
  if (limited.length >= 3) {
    formatted += ")";
  }
  if (limited.length > 3) {
    formatted += ` ${limited.slice(3, 6)}`;
  }
  if (limited.length > 6) {
    formatted += `-${limited.slice(6, 8)}`;
  }
  if (limited.length > 8) {
    formatted += `-${limited.slice(8, 10)}`;
  }

  return formatted;
}

export function isValidRussianPhone(value = "") {
  return /^\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}$/.test(value);
}

export function removePhoneDigit(value = "", cursor = 0, direction = "backward") {
  const digits = String(value).replace(/\D/g, "");
  const normalized = digits.startsWith("7")
    ? digits.slice(1)
    : digits.startsWith("8")
    ? digits.slice(1)
    : digits;

  if (!normalized.length) {
    return "";
  }

  const digitsBeforeCursor = String(value.slice(0, cursor)).replace(/\D/g, "").length;
  const fixedPrefixDigits = value.startsWith("+7") ? 1 : 0;
  const normalizedDigitsBeforeCursor = Math.max(digitsBeforeCursor - fixedPrefixDigits, 0);

  const deleteIndex =
    direction === "forward"
      ? normalizedDigitsBeforeCursor
      : normalizedDigitsBeforeCursor - 1;

  if (deleteIndex < 0 || deleteIndex >= normalized.length) {
    return formatRussianPhone(normalized);
  }

  const nextDigits =
    normalized.slice(0, deleteIndex) + normalized.slice(deleteIndex + 1);

  return formatRussianPhone(nextDigits);
}
